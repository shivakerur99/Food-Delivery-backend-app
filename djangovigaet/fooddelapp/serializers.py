# serializer.py
from rest_framework import serializers
from .models import Organization, Item, Pricing

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'type', 'description']

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['organization', 'item', 'zone', 'base_distance_in_km', 'km_price', 'fix_price']
