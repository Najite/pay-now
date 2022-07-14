from django.urls import path
from .import views

app_name='transfer'
urlpatterns = [
    path('wallet/', views.add_fund_card, name='card_fund' ),
    path('fund-wallet/pin-verification/', views.pin_authentication, name='pin_authentication'),
    path('fund-wallet/otp/', views.otp_authentication, name='otp_authentication'),
    path('fund-wallet/transaction-complete/', views.complete_transaction, name='complete_transaction'),
    
    
]
