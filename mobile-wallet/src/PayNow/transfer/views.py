from django.shortcuts import render, redirect
from.forms import FundAccountForm, PinForm, OtpForm
from rave_python import Rave, Misc, RaveExceptions
import json
import requests
from rich import print_json
from wallet.models import Wallet



# Create your views here.
def pin_view(request):
    form = PinForm(request.POST)
    if form.is_valid():
        pin = form.cleaned_data['pin']
    
    return render(request, 'pin.html', {'form':form})     
    


def add_fund_card(request):
    form = FundAccountForm(request.POST)
    if form.is_valid():
        card_number = form.cleaned_data['card_number']
        full_name = form.cleaned_data['full_name']
        expiry_month = form.cleaned_data['expiry_month']
        expiry_year = form.cleaned_data['expiry_year']
        cvv = form.cleaned_data['cvv']
        amount = form.cleaned_data['amount']
        email = form.cleaned_data['email']
        
        
        # everything flutterwave
        auth_token = 'FLWSECK_TEST-8631e24e08584b518d6e850dda0f556e-X'
        hed = {'Authorization':'Bearer ' + auth_token}
        
        data = {
            'cardno': card_number,
            'fullname': full_name,
            'expirymonth': expiry_month,
            'expiryyear': expiry_year,
            'cvv': cvv,
            'amount':amount,
            'email':email,           
            
         }
         
        rave = Rave('FLWPUBK_TEST-5359bc14f0f3ff04007583f80f74818b-X','FLWSECK_TEST-14a1c5d9fe2cfaa4a386b915473ea0ab-X', usingEnv=False )
        
        try:
            
            response = rave.Card.charge(data)
            request.session['data'] = data
            response = json.dumps(response, indent=3, sort_keys=True)
            print_json(response)
            response = json.loads(response)
        
            if response["suggestedAuth"]:
                arg = Misc.getTypeOfArgsRequired(response["suggestedAuth"])            
                if arg == "pin":
                    request.session['response'] = response                
                    return redirect('transfer:pin_authentication') 
        
        except RaveExceptions.CardChargeError as e:
            
            print(e.rr['errMsg'])
            print(e.err["flwRef"])
            
        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])

        

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])
                
            
    return render(request, 'card.html', {'form':form})


#pin verification
def pin_authentication(request): 
    data = request.session['data']
    form = PinForm(request.POST)
    rave = Rave('FLWPUBK_TEST-5359bc14f0f3ff04007583f80f74818b-X','FLWSECK_TEST-14a1c5d9fe2cfaa4a386b915473ea0ab-X', usingEnv=False )
    response = request.session['response']
    
    if form.is_valid():
        pin = form.cleaned_data['pin']
        
        try:
            
            Misc.updatePayload(response["suggestedAuth"], data, pin=pin)
            print('my pin', pin)
            response = rave.Card.charge(data)
            print('my response', response)
        
            if response["validationRequired"]:
                request.session['response'] = response
                print('my otp validation', response)
                return redirect('transfer:otp_authentication')
        
        except RaveExceptions.CardChargeError as e:
            
            print(e.rr['errMsg'])
            print(e.err["flwRef"])
            
        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])

        

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])
    
    return render(request, 'pin.html', {'form':form})


def otp_authentication(request):
    form = OtpForm(request.POST)
    rave = Rave('FLWPUBK_TEST-5359bc14f0f3ff04007583f80f74818b-X','FLWSECK_TEST-14a1c5d9fe2cfaa4a386b915473ea0ab-X', usingEnv=False )
    response = request.session['response']
    print('otp authenticaation response', response)
    if form.is_valid():
        otp = form.cleaned_data['otp']
        request.session['otp'] = otp
        print('my otp', otp)
        
        try:        
            rave.Card.validate(response["flwRef"], f'{otp}')
            response = rave.Card.verify(response["txRef"])
            request.session['response'] = response
            print('my response', response)
            
        except RaveExceptions.CardChargeError as e:
            
            print(e.rr['errMsg'])
            print(e.err["flwRef"])
            
        except RaveExceptions.TransactionValidationError as e:
            print(e.err)
            print(e.err["flwRef"])

        

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txRef"])
        
        
        return redirect('transfer:complete_transaction')
        
    return render(request, 'otp.html', {'form':form})
        

def complete_transaction(request):
    response = request.session['response']
    print('transaction response', response)
    
    try:
        
        if response['transactionComplete']:
            wallet = Wallet.objects.get(wallet=request.user)
            wallet.balance += response['chargedamount']
            wallet.save()
            
            return redirect('wallet:dashboard')
            
        
    except RaveExceptions.TransactionValidationError as e:
        print(e.err['errMsg'])
        print(e.err["flwRef"])
        
    except RaveExceptions.TransactionChargeError as e:
        print(e.rr['errMsg'])
        print(e.rr['txRef'])
        