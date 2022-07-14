from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    wallet = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    account_number = models.IntegerField()
    bank = models.CharField(max_length=20)    
    
    def __str__(self):
        return self.wallet.username
    