from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=8, null=True)
    course = models.CharField(max_length=250, null=True)
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

