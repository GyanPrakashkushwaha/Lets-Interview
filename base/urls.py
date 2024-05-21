from django.urls import path
from . import views


urlpatterns = [
    path(route='',view=views.home,name='home'),
    path(route='room/',view=views.room,name="room")
]
