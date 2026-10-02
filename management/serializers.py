from rest_framework import serializers
from .models import Vehicle

class RegisterVehicleSerializer(serializers.ModelSerializer):
    model = serializers.CharField(required=True, max_length=100)
    price = serializers.DecimalField(max_digits=12, decimal_places=2, required=True)
    year_of_manufacture = serializers.IntegerField()
    make = serializers.CharField(required=True, max_length=50)
    imported = serializers.BooleanField()
    color = serializers.CharField(required=True, max_length=50)

    class Meta:
        model = Vehicle
        fields = ['model', 'price', 'year_of_manufacture', 'make', 'imported', 'color']

class ListAllVehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'model', 'price', 'year_of_manufacture', 'make', 'imported', 'color']

class ListOneVehicleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Vehicle
        fields = ['id', 'model', 'price', 'year_of_manufacture', 'make', 'imported', 'color']

class UpdateVehicleSerializer(serializers.ModelSerializer):
        model = serializers.CharField(required=True, max_length=100)
        price = serializers.DecimalField(max_digits=12, decimal_places=2, required=True)
        year_of_manufacture = serializers.IntegerField()
        make = serializers.CharField(required=True, max_length=50)
        imported = serializers.BooleanField()
        color = serializers.CharField(required=True, max_length=50)

        class Meta:
            model = Vehicle
            fields = ['model', 'price', 'year_of_manufacture', 'make', 'imported', 'color']
