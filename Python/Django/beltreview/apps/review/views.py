# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from models import User


def index(request):
    return render(request, 'review/index.html')


def register(request):
    errors_user = User.objects.validate_registration(request.POST)

    if errors_user[0]:
        for fail in errors_user[0]:
            messages.error(request, fail)
        return redirect('/')
    request.session['id'] = errors_user[1].id
    return redirect('/')


def login(request):
    errors_login = User.objects.validate_login(request.POST)

    if errors_login[0]:
        for fail in errors_login[0]:
            messages.error(request, fail)

        return redirect('/')

    request.session['id'] = errors_login[1].id
    return redirect('/success')


def success(request):
    if not "id" in request.session.keys():
        print "Not logged in"
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, "review/success.html", context)
