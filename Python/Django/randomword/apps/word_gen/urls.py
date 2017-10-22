from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^word_gen$', views.word_gen),
    url(r'^generate$', views.generate)

]
