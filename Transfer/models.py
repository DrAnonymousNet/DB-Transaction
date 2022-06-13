from enum import unique
from django.db import models

# Create your models here.


class Account(models.Model):
    account_num = models.BigIntegerField( unique=True)
    balance = models.FloatField()

    
        
    
    def __str__(self) -> str:
        return f"{self.account_num}"

    def get_balance(self) -> float:
        return self.balance


