from django.urls import path
from . import views
from wallet.views import dashboard

app_name='service'
urlpatterns = [
    path('<slug:slug>/', views.Service_details, name='service'),
    path('category/<slug:slug>/', dashboard, name='category'),
    
]
