from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    customer_id = models.AutoField(primary_key=True)

class PurchaseOrder(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchase_orders')


    def save(self, *args, **kwargs):
        if self.pricing > self.mrp:
            raise ValueError("Pricing cannot be greater than MRP.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase Order #{self.purchase_order_id} - {self.product_name}"

class ShippingDetails(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='shipment_details')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shipments')