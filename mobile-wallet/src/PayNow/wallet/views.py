from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .forms import VirtualAccountForm
from.models import Wallet
from rich import print_json
import requests
import json
from django.contrib.auth.decorators import login_required
from service.models import Service, Category

# Create your views here.

def dashboard(request, slug=None):    
    category = None
    services = Service.objects.all()
    categories = Category.objects.all()
    wallet = Wallet.objects.filter(wallet=request.user).first()    
    if slug:
        category = get_object_or_404(Category, slug=slug)
        services = services.filter(category=category)
    
    return render(request, 'dashboard.html', {'wallet':wallet,
                                              'categories':categories,
                                              'services':services})


@login_required(login_url='account:login')
def create_virtual_account(request):
    form = VirtualAccountForm(request.POST)
    if form.is_valid():  
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        bvn = form.cleaned_data['bvn']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        
        wallet = request.user
        auth_token = 'FLWSECK_TEST-14a1c5d9fe2cfaa4a386b915473ea0ab-X'
        hed = {'Authorization':'Bearer ' + auth_token}
        data = {
                'email': email,
                'is_permanent':True,
                'bvn':bvn,
                'phonenumber':phone_number,
                'firstname':first_name,
                'lastname':last_name,  
            }        
            
        url = 'https://api.flutterwave.com/v3/virtual-account-numbers'
        response = requests.post(url, json=data, headers=hed)
        
        response = json.dumps(response.json(), indent=3, sort_keys=True)
        print_json(response)
        
        data = json.loads(response)     
        
        
        wallet.save()
        Wallet.objects.create(wallet=wallet,
                                account_number= data['data']['account_number'],
                                bank=data['data']['bank_name'])
        
        return redirect('wallet:dashboard')         
        
    
    return render(request, 'account.html', {'form':form})

        

        
    
    
    
    
