from django.urls import path
from . import views

#Create path for views pages
urlpatterns = [
    path('', views.home, name='fpl-home'),
]