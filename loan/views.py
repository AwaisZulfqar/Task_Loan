
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth import authenticate ,login,logout
from .forms import *
# Create your views here.

class RegisterView(View):
    def get(self,request):
        fm = RegisterForm()
        return render(request,"register.html",{"form":fm})
        
    def post(self,request):
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("login")
        return render(request,"register.html",{"form":fm})
        


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()  
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate(username=username,password=password)
            login(request, form.get_user())  
            print("User logged in:", request.user)  
            return redirect('bankcreate') 
        return render(request, "login.html", {"form": form})  

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')



class BankCreateView(View):
    def get(self,request):
            fm = BankForm()
            return render(request,'bankcreate.html',{"form":fm})

    def post(self,request):
            fm = BankForm(request.POST)
            if fm.is_valid():
                fm.save()
            return render(request,'bankcreate.html',{"form":fm})
        
        


class BankListView(View):
     def get(self,request):
        bank = Bank.objects.all()
        return render(request,'banklist.html',{"banks":bank})
     def post(self,request):
            bank = Bank.objects.all()
            return render(request,'banklist.html',{"banks":bank})




               
