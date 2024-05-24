from django.shortcuts import render
from .models import Room
from .forms import RoomForm


allRooms = [
    {'id': 1,'name':"interview"},
    {'id': 2,'name':"job discussion"},
    {'id': 3,'name':"About Questions"},
]

# Create your views here.
def home(request):
    # data available in the dabase to get that we need to use this code.
    allRooms = Room.objects.all()
    dictToPass = {"room": allRooms}
    
    return render(request=request,template_name="base/home.html",context=dictToPass)

def room(request,pk):
    # context dictionary
    """ to render the data into the page, I have to pass the data into the render method using a dictionary.
    I will only be able to get the data to the htlm page for rendering using the key of the dictionary. """
    
    rm = Room.objects.get(id=pk)
            
    context = {"rm": rm}
    
    # in html file I can do all the things I want using the "room" key.
    return render(request=request,template_name="base/room.html",context=context)


def createRoom(request):
    form_formate = RoomForm()
    context = {'forms':form_formate}
    return render(request=request,template_name='base/room_form.html',context=context)