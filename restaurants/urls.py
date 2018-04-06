from django.urls import path
from . import  views
app_name = 'restaurants'
urlpatterns = [
    path('',views.showRestaurants, name = 'showrestaurants'),
    path('restaurant/new',views.newRestaurants,  name = 'newrestaurant'),
    path('restaurant/<int:restaurant_id>/edit',views.editRestaurant,  name = 'editrestaurant'),
    path('restaurant/<int:restaurant_id>/delete',views.deleteRestaurant, name = 'deleterestaurant'),
    path('restaurant/<int:restaurant_id>/menu',views.showMenu, name = 'showmenu'),
    path('restaurant/<int:restaurant_id>/menu/new',views.newMenuItem, name = 'newmenuitem'),
    path('restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',views.editMenuItem, name = 'editmenuitem'),
    path('restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',views.deleteMenuItem, name = 'deletemenuitem'),
               ]

