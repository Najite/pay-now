from django.urls import path
from . import views

app_name='wallet'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('account-creation', views.create_virtual_account, name='account'),
        
    
]
