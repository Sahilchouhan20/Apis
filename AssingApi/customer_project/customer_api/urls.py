from django.urls import path
from .views import CustomerList, PurchaseOrderList, ShippingDetailsList, CustomerShipmentList, CustomerPurchaseOrderList

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('purchase-orders/', PurchaseOrderList.as_view(), name='purchase-order-list'),
    path('shipping-details/', ShippingDetailsList.as_view(), name='shipping-details-list'),
    path('customer-shipments/<str:city>/', CustomerShipmentList.as_view(), name='customer-shipment-list'),
    path('customer-purchase-orders/', CustomerPurchaseOrderList.as_view(), name='customer-purchase-order-list'),
]