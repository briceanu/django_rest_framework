import uuid
from django.db import models
# from drivers.serializers import DriverSerializer
from truck.models import Truck
from django.contrib.auth.models import User

# Create your models here.

    
class WorkingDayModel(models.Model):
    worker_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(User,to_field='username',on_delete=models.CASCADE,default='')
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    load_carried = models.PositiveIntegerField(null=False)
    fuel_consumption = models.PositiveIntegerField(null=False)
    km_driven = models.PositiveIntegerField(null=False) 
    truck_used = models.ForeignKey(Truck, to_field='registration_plate', on_delete=models.CASCADE ,default="")
