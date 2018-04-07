from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant,MenuItem


def showRestaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants.html', {'restaurants': restaurants})


def newRestaurants(request):
    if request.method == 'POST':
        newRest = Restaurant(name = request.POST['newrest'])
        newRest.save()
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/newrestaurant.html')

def editRestaurant(request, restaurant_id):
    editedRestaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        editedRestaurant.name = request.POST['editrest']
        editedRestaurant.save()
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/editrestaurant.html', {'restaurant': editedRestaurant})


def deleteRestaurant(request, restaurant_id):
    deletedRestaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        deletedRestaurant.delete()
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/deleterestaurant.html', {'restaurant' : deletedRestaurant})

def showMenu(request, restaurant_id):
    
    return HttpResponse("Show Menu %s" %restaurant_id)

def newMenuItem(request, restaurant_id):
    
    return HttpResponse("New menu item of %s" %restaurant_id)

def editMenuItem(request, restaurant_id, menu_id):
    
    return HttpResponse("Edit Menu Item %s of %s" % (menu_id ,restaurant_id))

def deleteMenuItem(request, restaurant_id, menu_id):
    
    return HttpResponse("Delete menu item %s of %s" % (menu_id, restaurant_id))