# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login


from GroupBuyApp.models import *

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                return HttpResponse('Login complete!')
            else:
                return render(
                    request,
                    'login_form.html',
                    {login_form: login_form})
    else:
        form = LoginForm()
        return render(
            request,
            'login_form.html',
            {'login_form': form})

def main(request):
    return render(request, 'main.html')
