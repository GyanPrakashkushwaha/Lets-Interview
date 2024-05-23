from django.shortcuts import render , HttpResponse


allRooms = [
    {'id': 1,'name':"interview"},
    {'id': 2,'name':"job discussion"},
    {'id': 3,'name':"About Questions"},
]

# Create your views here.
def home(request):
    dictToPass = {"room": allRooms}
    
    return render(request=request,template_name="base/home.html",context=dictToPass)

def room(request,pk):
    # context dictionary
    """ to render the data into the page, I have to pass the data into the render method using a dictionary.
    I will only be able to get the data to the htlm page for rendering using the key of the dictionary. """
    
    rm = None
    for i in allRooms:
        if i['id'] == int(pk):
            rm = i
            
    context = {"rm": rm}
    
    # in html file I can do all the things I want using the "room" key.
    return render(request=request,template_name="base/room.html",context=context)