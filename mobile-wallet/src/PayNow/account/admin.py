from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from wallet.models import Wallet

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name ='user'    

class WalletAdmin(admin.StackedInline):
    model = Wallet
    fk_name = 'wallet'
    
    
    
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, WalletAdmin,)
    
    def get_profile_location(self, instance):
        return instance.profile.location 
    get_profile_location.short_description = 'Location'
    
    def get_wallet_location(self, instance):
        return instance.wallet.location
    get_profile_location.short_description = 'Location'
    
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)