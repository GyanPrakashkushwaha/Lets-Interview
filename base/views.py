from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return render(request=request,template_name="base/home.html")

allRooms = [
    {'id': 1,'name':"interview"},
    {'id': 2,'name':"job discussion"},
    {'id': 3,'name':"About Questions"},
]
def room(request):
    # context dictionary
    """ to render the data into the page, I have to pass the data into the render method using a dictionary.
    I will only be able to get the data to the htlm page for rendering using the key of the dictionary. """
    
    dictToPass = {"room": allRooms}
    # in html file I can do all the things I want using the "room" key.
    return render(request=request,template_name="base/room.html",context=dictToPass)