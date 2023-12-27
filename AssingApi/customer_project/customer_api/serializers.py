from rest_framework import serializers
from .models import Customer, PurchaseOrder, ShippingDetails

class ShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetails
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    shipment_details = ShippingDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    purchase_orders = PurchaseOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'