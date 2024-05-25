from django.shortcuts import render , redirect
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
    if request.method == 'POST':
        form_formate = RoomForm(request.POST) # parsing all the values.
        print(request.POST)
        if form_formate.is_valid:
            form_formate.save() # this is saving the forms value to the DB
            return redirect(to='home') # if the form is sucessfully saved then I will be redirected to home page.
            
    context = {'forms':form_formate}
    return render(request=request,template_name='base/room_form.html',context=context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request=request,template_name='base/room_form.html',context=context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request=request,template_name='base/delete.html',context=context)
    