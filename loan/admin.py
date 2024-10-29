from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['owner','name',]

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['bank','name','amount',]

@admin.register(Loan_Taker)
class LoanTakerAdmin(admin.ModelAdmin):
    list_display = ['account','take_by','loan_amount','mark_up','took_at','approved',]

