# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

        if not self.filter(email_address = post_data['email_address']):
            return user
            #errors.append('Invalid credentials')

        else:
            user = self.get(email_address=post_data['email_address'])
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

        if self.filter(email_address=post_data['email_address']):
            errors.append("Email in use")

        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters")

        if post_data['password'] != post_data['passwordconfirm']:
            errors.append("Passwords does not match")

        if not errors:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            user = self.create(
                full_name = post_data['full_name'],
                username = post_data['username'],
                email_address = post_data['email_address'],
                password = hashed_pw,
                )
        return errors, user


class User(models.Model):

    full_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
