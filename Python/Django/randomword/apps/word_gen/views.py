# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):

        return HttpResponse("hellow_world")

def word_gen(request):
        if request.session.get('count') is None:
            request.session['count'] = 0
        if request.session.get('word') is None:
            request.session['word'] = ""
        request.session['count'] += 1
        context = {
            "count": request.session['count'],
            "word": request.session['word']
            }
        return render(request, 'word_gen/index.html', context)

def generate(request):

    request.session['word'] = get_random_string(length=32)

    return redirect('/word_gen')
