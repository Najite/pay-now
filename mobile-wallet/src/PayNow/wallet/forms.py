from django import forms
from django.forms import ValidationError
class VirtualAccountForm(forms.Form):
    first_name = forms.CharField(
        widget = forms.TextInput
        )
    
    last_name = forms.CharField(
        widget = forms.TextInput
    )
    
    bvn = forms.CharField(
        widget=forms.NumberInput
    )
    
    email = forms.EmailField()
    
    phone_number = forms.CharField(
        widget = forms.NumberInput()
    )
    



    
    
        
    
    
    
    