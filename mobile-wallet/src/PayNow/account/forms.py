from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from.models import Profile


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
    
        
class LoginForm(AuthenticationForm):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'id':'form2Example17'
        })
    
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 label='First Name',
                                 widget=forms.TextInput(
                                     attrs={'class':'form-outline form-control', 'id':'form3Example1',
                                    }))
       
    last_name = forms.CharField(max_length=100,
                                label='Last Name',
                                widget=forms.TextInput(
                                    attrs={'class':'form-outline form-control', 'id':'form3Example2',
                                    })
                                )
    
    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
        attrs={'class':'form-outline form-control',
               'id':'form3Example3',
               })
        )
        
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']
        
    
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'id':'form3Example1',
            
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
            'id':'form3Example2',
            
        })
        
        self.fields['username'].widget.attrs.update({
            'class':'form-control form-control-lg',
            'id':'form3Example2 form2Example17'
        })
        
        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
            'id':'form3Example3',
            
        })
        
        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
            'id':'form3Example3'
        })
        
    
        
               
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
        
        