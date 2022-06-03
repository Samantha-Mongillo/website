

from django.urls import path
from . import views

#creating path for website
urlpatterns = [
   path('', views.homepage), 
   path('count/', views.count, name='count'),
]
