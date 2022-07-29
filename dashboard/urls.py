from django.urls import path
from . import views

#Create path for views pages
urlpatterns = [
    path('dashboard/', views.dashboard, name='fpl-dashboard'),
] 