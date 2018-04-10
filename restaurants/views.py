from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant,MenuItem
from django.contrib import messages
from django.http import JsonResponse


def showRestaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants.html', {'restaurants': restaurants})


def newRestaurants(request):
    if request.method == 'POST':
        newRest = Restaurant(name = request.POST['newrest'])
        newRest.save()
        messages.add_message(request, messages.SUCCESS,'Restaurant was created')
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/newrestaurant.html')

def editRestaurant(request, restaurant_id):
    editedRestaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        editedRestaurant.name = request.POST['editrest']
        editedRestaurant.save()
        messages.add_message(request,messages.SUCCESS, 'Restaurant was edited!')
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/editrestaurant.html', {'restaurant': editedRestaurant})


def deleteRestaurant(request, restaurant_id):
    deletedRestaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        deletedRestaurant.delete()
        messages.add_message(request, messages.SUCCESS, 'Restaurant was deleted!')
        return HttpResponseRedirect(reverse('restaurants:showrestaurants'))
    else:
        return render(request,'restaurants/deleterestaurant.html', {'restaurant' : deletedRestaurant})

def showMenu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    items = MenuItem.objects.filter(restaurant_id = restaurant)
    return render(request, 'restaurants/menu.html', {'restaurant':restaurant, 'items': items})

def newMenuItem(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        newMenuItem = MenuItem(name = request.POST['namemenu'], description = request.POST['descripmenu'],
                               course = request.POST['coursemenu'], price = request.POST['pricemenu'],
                               restaurant_id = restaurant)
        newMenuItem.save()
        messages.add_message(request, messages.SUCCESS, 'Menu item was created!')
        return HttpResponseRedirect(reverse('restaurants:showmenu', args = [restaurant_id]))
    else:
        return render(request,'restaurants/newmenuitem.html', {'restaurant' :restaurant})

def editMenuItem(request, restaurant_id, menu_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    editedMenu = MenuItem.objects.get(id = menu_id, restaurant_id = restaurant)
    if request.method == 'POST':
        if request.POST['namemenu']:
            editedMenu.name = request.POST['namemenu']
        if request.POST['descripmenu']:
            editedMenu.description = request.POST['descripmenu']
        if request.POST['coursemenu']:
            editedMenu.course = request.POST['coursemenu']
        if request.POST['pricemenu']:
            editedMenu.price = request.POST['pricemenu']
        editedMenu.save()
        messages.add_message(request, messages.SUCCESS, 'Menu item was edited')
        return HttpResponseRedirect(reverse('restaurants:showmenu', args = [restaurant_id]))
    else:
        return render(request,'restaurants/editmenuitem.html',{'restaurant' : restaurant, 'item' : editedMenu})

def deleteMenuItem(request, restaurant_id, menu_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    deletedMenu = MenuItem.objects.get(id = menu_id, restaurant_id = restaurant)
    if request.method == 'POST':
        deletedMenu.delete()
        messages.add_message(request, messages.SUCCESS, 'Menu item deleted')
        return HttpResponseRedirect(reverse('restaurants:showmenu', args = [restaurant_id]))
    else:
        return render(request,'restaurants/deletemenuitem.html',{'restaurant' : restaurant, 'item' : deletedMenu})

#Api Endpoints
def showRestaurantsJSON(request):
    restaurants = Restaurant.objects.all()
    Restaurants = [restaurant.serialize for restaurant in restaurants]
    return JsonResponse(data= Restaurants, safe= False)

def showmenuJSON(request,restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    items =  MenuItem.objects.filter(restaurant_id = restaurant)
    itemsjson = [item.serialize for item in items]
    return JsonResponse(data = itemsjson, safe = False)

def showMenuItemJSON(request, restaurant_id, menu_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    item = MenuItem.objects.get(id = menu_id, restaurant_id = restaurant)
    itemjson = [item.serialize]
    return JsonResponse(data= itemjson, safe= False)