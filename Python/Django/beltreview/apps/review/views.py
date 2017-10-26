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
            messages.error(request, fail, "register")
        return redirect('/')
    request.session['id'] = errors_user[1].id
    return redirect('/')


def login(request):

    # Check parameters are valid for login
    errors_login_params = User.objects.validate_login_params(request.POST)

    # There were errors in the parameters
    if errors_login_params:
        for fail in errors_login_params:
            messages.error(request, fail, "login")
        return redirect('/')

    # Check for user in DB
    user_record = User.objects.find_user(request.POST)

    # No user returned so tell user invalid login
    if user_record is None:
        messages.error(request, 'Invalid Credentials', "login")
        return redirect('/')

    # We have a user
    request.session['id'] = user_record.id

    return redirect('/success')


def success(request):
    if not "id" in request.session.keys():
        print "Not logged in"
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, "review/success.html", context)
