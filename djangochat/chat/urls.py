from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_id>', views.room, name='room'),
]
