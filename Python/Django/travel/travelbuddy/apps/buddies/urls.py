from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^travels$', views.travels),
    url(r'^add$', views.add),
    url(r'^createtrip$', views.createtrip),
    url(r'^addtrip/(?P<tripid>\d+)$',views.addtrip),
    url(r'^destination/(?P<tripid>\d+)$',views.destination),

]
