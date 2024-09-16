from rest_framework import serializers
from truck.models import Truck
from datetime import date


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"
    
    def validate_brand(self,value):
        brands = ["Scania R45","Mercedes Actros","Iveco Stralis"]
        if value.lower() not in [brand.lower() for brand in brands]:
            raise serializers.ValidationError('you can only choose: Scania R45, Mercedes Actros, Iveco Stralis')
        return value




    def validate_year_of_build(self, value):
        min_year_of_build = date(2020, 1, 1)
        if value < min_year_of_build:
            raise serializers.ValidationError('Year of build cannot be before January 1, 2020.')
        return value