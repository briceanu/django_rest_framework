from rest_framework import serializers

from truck.models import Truck
from .models import WorkingDayModel
from django.contrib.auth.models import User


class SerializerWorkingDayModel(serializers.ModelSerializer):
    truck_used = serializers.SlugRelatedField(
        queryset=Truck.objects.all(),
        slug_field='registration_plate'
    )
    class Meta:
        model = WorkingDayModel
        fields = "__all__"
    
  
    username = serializers.SlugRelatedField(
        queryset=User.objects.all(),  # This ensures that the provided username exists in the User model
        slug_field='username'
    )
    def validate_km_driven(self,value):
        if value <=0:
            raise serializers.ValidationError('numbers greater than 0 allowed')
        return value
    

class LimitedWorkingDayModelSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', read_only=True)
    truck_used = serializers.SlugRelatedField(slug_field='registration_plate', read_only=True)

    class Meta:
        model = WorkingDayModel
        fields = ['username', 'km_driven', 'truck_used']