from django.shortcuts import render
from django.http import HttpResponse



#class Index(request):
#    
#        return HttpResponse("Hello World with classes")
#def index(request):
#    return HttpResponse("hello World")
# Create your views here.

def showRestaurants(request):
    
    return HttpResponse("Show all restaurants")

def newRestaurants(request):
    
    return HttpResponse("New restaurant")

def editRestaurant(request, restaurant_id):
    
    return HttpResponse("Edit restaurant %s" %restaurant_id)

def deleteRestaurant(request, restaurant_id):
    
    return HttpResponse("delete restaurant %s" %restaurant_id)

def showMenu(request, restaurant_id):
    
    return HttpResponse("Show Menu %s" %restaurant_id)

def newMenuItem(request, restaurant_id):
    
    return HttpResponse("New menu item of %s" %restaurant_id)

def editMenuItem(request, restaurant_id, menu_id):
    
    return HttpResponse("Edit Menu Item %s of %s" % (menu_id ,restaurant_id))

def deleteMenuItem(request, restaurant_id, menu_id):
    
    return HttpResponse("Delete menu item %s of %s" % (menu_id, restaurant_id))