from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
def index(request):
    #return HttpResponse("om shanti")
    return HttpResponse("<h1 style=\"color:red\"> Om shanti </h1>")
"""
 
def name1(request):
    return HttpResponse("namaste name1")

  
def name2(request):
    return HttpResponse("namaste name2")

"""
def greet(request, name):
    #return HttpResponse(f"namaste {name}")
    return HttpResponse(f"namaste {name.capitalize()}")
"""

def index(request):
    return render(request, 'myapp/index.html')
    
def greet(request, name):
    return render(request, 'myapp/greet.html', {"name":name.capitalize()})
    
