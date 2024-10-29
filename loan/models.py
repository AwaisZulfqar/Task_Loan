from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class Loan_Taker(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    take_by = models.ForeignKey(User,on_delete=models.CASCADE)
    loan_amount = models.IntegerField()
    mark_up = models.CharField(max_length=3)
    took_at = models.DateField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.take_by
    
    

    