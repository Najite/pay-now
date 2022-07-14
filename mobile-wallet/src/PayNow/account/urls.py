from django.urls import path
from . import views


app_name='account'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registration', views.registration_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile' ),
    
    
]
