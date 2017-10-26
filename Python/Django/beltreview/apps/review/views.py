# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from models import User

# Create your views here.
def index(request):
    return render(request, 'review/index.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)

    if errors:
        for fail in errors:
            messages.error(request, fail)
        return redirect('/')

    return redirect('/')
