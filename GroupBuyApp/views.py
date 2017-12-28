# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import random
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
    user = auth.get_user(request)
    if user is not None:
        try:
            joined = AccountLot.objects.get(account_id=user.id, lot_id=lot_id) is not None
        except: joined = False

    else:
        joined = False
    return render(
        request,
        'buyInfo.html',
        {
            'lot': lot,
            'author': author,
            'user': auth.get_user(request),
            'joined': joined
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


def deleteLot(request):
    lot_id = request.GET['id']
    lot = Lot.objects.get(pk=lot_id)
    lot.delete()
    return redirect('/listBuy')

def join(request):
    user = auth.get_user(request)
    joinedTxt = request.GET['joined']
    joined = joinedTxt != 'True'
    if user is not None:
        lot_id = request.GET['id']
        lot = Lot.objects.get(pk=lot_id)
        author = lot.account
        if joined:
            lot.usersJoin += 1
            AccountLot.objects.create(account_id=user.id, lot_id=lot_id, time=datetime.datetime.now())
        else:
            lot.usersJoin -= 1
            AL = AccountLot.objects.get(account_id=user.id, lot_id=lot_id)
            AL.delete()

    return render(
        request,
        'buyInfo.html',
        {
            'lot': lot,
            'author': author,
            'user': auth.get_user(request),
            'joined': joined
        }
    )






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

def addMoney(request):
    account = Account.objects.get(pk = auth.get_user(request).id)
    account.cash += random.randint(100, 1000)
    account.save()
    #return redirect('/profile', id=account.user_id)
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
