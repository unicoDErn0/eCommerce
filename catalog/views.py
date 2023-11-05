# yourapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    Address = models.CharField(max_length=150)



class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/success/')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # replace 'success' with the name of your success page
    else:
        form = UserForm()
    return render(request, 'registration_page.html', {'form': form})

