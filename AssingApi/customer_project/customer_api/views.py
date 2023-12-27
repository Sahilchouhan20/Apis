from rest_framework import generics
from .models import Customer, PurchaseOrder, ShippingDetails
from .serializers import CustomerSerializer, PurchaseOrderSerializer, ShippingDetailsSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class ShippingDetailsList(generics.ListCreateAPIView):
    queryset = ShippingDetails.objects.all()
    serializer_class = ShippingDetailsSerializer

class CustomerShipmentList(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        return Customer.objects.filter(city=city)

class CustomerPurchaseOrderList(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customers = Customer.objects.all()
        return customers.prefetch_related('purchaseorder_set', 'purchaseorder_set__shipment_details')