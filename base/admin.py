from django.contrib import admin
from .models import Room, Topic, Message

# This is to see the and do CRUD operations in the admin pannel of the webpage of admin.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

