from django.db import models
import uuid
 
# Create your models here.



class Truck(models.Model):
    truck_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20, null=False)
    fuel_type = models.CharField(max_length=15, null=False)
    year_of_build = models.DateField(null=False)
    registration_plate = models.CharField(max_length=20, null=False, unique=True)