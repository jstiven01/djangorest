from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=8, null=True)
    course = models.CharField(max_length=250, null=True)
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    @property
    def serialize(self):
        #returns object data in easily serializable format
        return {'name':self.name,
                'description':self.description,
                'id':self.id,
                'price':self.price,
                'course':self.course
        }

