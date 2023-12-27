# Generated by Django 4.2.1 on 2023-12-27 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_orders', to='customer_api.customer'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipments', to='customer_api.customer'),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name='purchase_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_details', to='customer_api.purchaseorder'),
        ),
    ]