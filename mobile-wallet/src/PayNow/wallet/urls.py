from django.urls import path
from . import views

app_name='wallet'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-virtual-wallet', views.create_virtual_account, name='account'),
        
    
]
