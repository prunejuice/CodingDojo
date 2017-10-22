# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *

def index(request):
    return render(request, 'login/index.html')


def register(request):

    # errors = People.objects.basic_validator(request.POST)
    #     if len(errors):
    #         for len(errors):
    #             for tag, error in errors.iteritimes():
    #                 messages.error(request, error, extra_tags=tag)


        if request.POST['password'] == request.POST['confirmpassword']:
            People.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email'], password = request.POST['password'])
        else:
           print "Passwords dont match"
        return redirect('/')

def login(request):



        if not People.objects.filter(email_address = request.POST['email']):
            print "username doesent exist"
            return redirect('/')
        if not People.objects.filter(password = request.POST['password']):
            print "password incorrect"
            return redirect('/')
        else:
            return  redirect('/success')

def success(request):
    return render(request, 'login/success.html')
