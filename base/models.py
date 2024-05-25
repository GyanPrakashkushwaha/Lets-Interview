from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(to=Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    # To change the order we can use this.
    class Meta:
        ordering = ['-updated','-created']
    
    
class Message(models.Model):
    """ This class is going to be a message creator."""
    
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
        
    # This is one to many relationship. `on_delete` parameters shows that if the room gets deleted all the messages get deleted.
    room = models.ForeignKey(to=Room,on_delete=models.CASCADE)
    body = models.TextField()    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.body[:50]
    