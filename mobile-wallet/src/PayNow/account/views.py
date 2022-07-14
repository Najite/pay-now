from django.shortcuts import redirect, render
from django.contrib import messages
from.forms import RegistrationForm, ProfilePictureForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import Profile


# Create your views here.
    
def logout_view(request):
    logout(request)
    return redirect('account:login')
    

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}')
                return redirect('page:index')
            else:
                messages.error(request, 'invalid details')
        else:
            messages.error(request, 'invalid details')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})



    
    

def registration_view(request):
    if request.user.is_authenticated:
        redirect('page:index')
        
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)            
            messages.success(request, 'your account is created succesfully')
            return redirect('page:index')
        messages.error(request, 'unsuccessful')
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form':form}) 



def profile_view(request):
    user = request.user.profile
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = ProfilePictureForm()
    return render(request, 'profile.html', {'form':form})


def edit_profile(request):
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('page:index')
        
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form':form})


def profile_picture(request):
    if request.method == 'POST':
        profile_picture = ProfilePictureForm(request.POST, request.FILES)
        if profile_picture.is_valid():
            profile = Profile()
            profile.image = profile_picture.cleaned_data['image']
            profile.save()
            saved=True
           
            return redirect('account:profile')
        
    else:
        form = ProfilePictureForm()
    return render(request, 'profile.html', {'form':form})
        
        