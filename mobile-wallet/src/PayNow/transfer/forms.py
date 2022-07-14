from django import forms

class FundAccountForm(forms.Form):
    amount = forms.CharField(
        widget=forms.NumberInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'Enter amount',
            'size':'17',
            'id':'typeExp',
            'minlength':'19',
            'maxlength':'19'
                
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'mymain@mail.com',
            'size':'17',
            'id':'typeExp',
            'minlength':'19',
            'maxlength':'19'
                
            }
        )
    )
    
    card_number = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class':'form-control form-control-lg',
            'placeholder':'1234 5678 9012 3457',
            'size':'17',
            'id':'typeExp',
            'minlength':'19',
            'maxlength':'19'
            
            
        })
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'Card Holder Name',
            'size':'17',
            'id':'typeName',
            
            }
        )
    )
    expiry_month = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'MM',
            'size':'7',
            'id':'exp',
            'minlength':'2',
            'maxlength':'2',
                        
            }
        )
    )
    expiry_year = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'YYYY',
            'size':'7',
            'id':'typeExp',
            'minlength':'2',
            'maxlength':'2',
                        
            }
        )
    )
    
    cvv = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            'class':'form-control form-control-lg',
            'placeholder':'cvv',
            'size':'1',
            'id':'typeText2',
            'minlength':'3',
            'maxlength':'3',
                        
            }
        )
    )
    
    
    
    

class PinForm(forms.Form):
    pin = forms.CharField(
        widget = forms.NumberInput
    )
    
class OtpForm(forms.Form):
    otp = forms.CharField(
        widget=forms.NumberInput
    )
    
    def otp_clean_data(self):
        otp = self.cleaned_data['otp']
        return otp
    
    
    
    