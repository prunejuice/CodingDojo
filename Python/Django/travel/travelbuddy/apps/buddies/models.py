# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
import bcrypt


class UserManager(models.Manager):


    def validate_login_params(self, post_data):
        errors = []

        # check you have email and password
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors.append("Please fill in all fields")

        return errors

    def find_user(self, post_data):

        user = None

        if not self.filter(username = post_data['username']):
            return user
            #errors.append('Invalid credentials')

        else:
            user = self.get(username=post_data['username'])
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                return user#errors.append('Invalid credentials')

        return user

    def validate_registration(self, post_data):

        errors = []
        user = None
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors.append("Please fill in all fields")
                break
        if len(post_data['full_name']) < 2:
            errors.append("Name field must be 2 or more characters")

        if len(post_data['username']) < 2:
            errors.append("Alis field must be 2 or more characters")

        if self.filter(username=post_data['username']):
            errors.append("Username in use")

        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters")

        if post_data['password'] != post_data['passwordconfirm']:
            errors.append("Passwords does not match")

        if not errors:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            user = self.create(
                full_name = post_data['full_name'],
                username = post_data['username'],
                password = hashed_pw,
                )
        return errors, user


class User(models.Model):

    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class TripManager(models.Manager):

    def validate_trip(self, request):
            errors = []
            trip = None
            for field, value in request.POST.iteritems():
                if len(value) < 1:
                    errors.append("Please fill in all fields")
                    break
            if len(request.POST['destination']) < 2:
                errors.append("Name field must be 2 or more characters")

            if len(request.POST['plan']) < 2:
                errors.append("Plan field must be 2 or more characters")

            startdate = request.POST['date_start']
            enddate = request.POST['date_end']

            formatted_startdate = datetime.strptime(enddate, '%Y-%m-%d')
            formatted_enddate = datetime.strptime(startdate, '%Y-%m-%d')
            todaysdate = datetime.today()

            if formatted_startdate < todaysdate:
                errors.append("Date must be in the future")

            if  formatted_startdate < formatted_enddate:
                    errors.append("End date must be after start date")

            user = User.objects.get(id=request.session['id'])
            if not errors:
                trip = self.create(
                        destination = request.POST['destination'],
                        plan = request.POST['plan'],
                        date_start = request.POST['date_start'],
                        date_end = request.POST['date_end'],
                        planner = user
                        )
                trip.traveler.add(user)
            return errors, trip


class Trip(models.Model):

        destination = models.CharField(max_length = 255)
        plan = models.CharField(max_length = 255)
        date_start = models.DateField()
        date_end = models.DateField()
        planner = models.ForeignKey(User,related_name='planner',null=True)
        traveler = models.ManyToManyField(User,related_name='travelfriends',null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        objects = TripManager()
