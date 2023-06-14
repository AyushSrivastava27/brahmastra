from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event', views.event, name='event'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('complaint', views.complaint, name='complaint'),
    path('organizer', views.organizer, name='organizer'),
    path('add', views.add, name = 'add'),
    path('edit', views.edit, name = 'edit'),
    path('update/<str:id>', views.update, name = 'update'),
    path('delete/<str:id>', views.delete, name= 'delete'),
    path('score', views.score, name = 'score'),
]