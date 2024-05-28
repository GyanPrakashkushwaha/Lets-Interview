from django.shortcuts import render , redirect
from .models import Room , Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username)
        except:
            messages.error(request, "User does not exist.")
            print(messages.error(request, "User does not exist."))
    
    context = {}
    return render(request, 'base/signup_login.html', context)

# Create your views here.
def home(request):
    # data available in the dabase to get that we need to use this code.
    # allRooms = Room.objects.all()
    
    # Now because I am creating search functionality by clicking to the sidbar that's why i don't want the above code.
    q = request.GET.get('q') # fetching q value from html page.
    
    # if q:
    #     rooms = Room.objects.filter(topic__name__icontains=q) # Here I want to fetch topic that's why written topic that had in model. And want to query for q that's why given topic__name = q.
    # else:
    #     rooms = Room.objects.all()
        
    # to search by name or description or topic name, I have to use models Q method because the above code don't gonna work.
    # The let's use & and or operations.
    
    if q:
        rooms = Room.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains = q) |
            Q(description__icontains = q))
    else:
        rooms = Room.objects.all()
    
    # topic for search.
    topics = Topic.objects.all()
    
    room_count = rooms.count()

    dictToPass = {"room": rooms,'topics':topics,'rooms_cnt':room_count}
    
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
            
    context = {'form':form_formate}
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
    