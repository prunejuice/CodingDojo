# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from models import *


def index(request):
    return render(request, 'buddies/index.html')


def register(request):
    errors_user = User.objects.validate_registration(request.POST)

    if errors_user[0]:
        for fail in errors_user[0]:
            messages.error(request, fail, "register")
        return redirect('/')
    request.session['id'] = errors_user[1].id
    return redirect('/travels')


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

    return redirect('/travels')

def logout(request):
    context = {
        'logout': request.session.pop('id')
    }
    return render(request,'buddies/index.html', context)

def success(request):
    if not "id" in request.session.keys():
        print "Not logged in"
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, "buddies/success.html", context)

def add(request):

    return render(request, 'buddies/add.html')

def travels(request):
    if not "id" in request.session.keys():
        print "Not logged in"
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    mytrips = Trip.objects.filter(traveler=request.session['id'])
    friends_trips = Trip.objects.all().exclude(traveler=user)

    context = {
        'user': user,
        'mytrips': mytrips,
        'friends_trips': friends_trips,
    }
    return render(request, 'buddies/travels.html', context)

def createtrip(request):
        errors_trip = Trip.objects.validate_trip(request)
        if errors_trip[0]:
            for fail in errors_trip[0]:
                messages.error(request, fail, "createtrip")
            return redirect('/add')
        return redirect('/travels')


def addtrip(request, tripid):

    trip = Trip.objects.get(id=tripid)
    user = User.objects.get(id=request.session['id'])
    trip.traveler.add(user)
    trip.save()
    return redirect('/travels')

def destination(request, tripid):
    user = User.objects.get(id=request.session['id'])
    trip = Trip.objects.get(id=tripid)
    alltravelers = trip.traveler.all()

    context = {
        'trip': trip,
        'user': user,
        'alltravelers': alltravelers,
    }
    return render(request, 'buddies/destinations.html', context)
