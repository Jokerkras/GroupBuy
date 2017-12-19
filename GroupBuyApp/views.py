# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django import forms
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf

from GroupBuyApp.models import *


def lots_list(request):
    lots = Lot.objects.all()
    return render(request, 'listBuy.html', {
        "lots": lots,
        'user': auth.get_user(request)
    })


def lot_details(request):
    lot_id = request.GET['id']
    lot = Lot.objects.get(pk=lot_id)
    author = Account.objects.get(pk=lot.account.user_id)
    return render(
        request,
        'buyInfo.html',
        {
            'lot': lot,
            'author': author,
            'user': auth.get_user(request)
        }
    )


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/listBuy')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/listBuy')


def profile_details(request):
    account_id = request.GET['id']
    account = Account.objects.get(pk=account_id)
    return render(
        request,
        'profile.html',
        {
            'account': account,
            'user': auth.get_user(request)
        }
    )


def main(request):
    return render(request, 'main.html')
