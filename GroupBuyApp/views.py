# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

from GroupBuyApp.models import *


def lots_list(request):
    lots = Lot.objects.all()
    return render(request, 'listBuy.html', {
        "lots": lots
    })


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput)


def login(request):
    if request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            user = authenticate(
                request,
                username=login.cleaned_data['username'],
                password=login.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                return HttpResponse('Login complete!')
            else:
                return render(
                    request,
                    'login.html',
                    {login: login})
    else:
        form = LoginForm()
        return render(
            request,
            'login.html',
            {'login': form})


def main(request):
    return render(request, 'main.html')
