from django.shortcuts import render
from typing import List
from django.core.exceptions import ImproperlyConfigured
from django.http.response import HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.

def user_signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      return HttpResponseRedirect('/accounts/login/')
  else:
    form = SignUpForm()
  return render(request, 'registration/signup.html', {'form':form}) 



def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
          uname = form.cleaned_data['username']
          upass = form.cleaned_data['password']

          user = authenticate(username=uname, password=upass)

          if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !!')
            return HttpResponseRedirect('/')
            
    else:
      form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})
  else:
    return HttpResponseRedirect('/')


def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/')
