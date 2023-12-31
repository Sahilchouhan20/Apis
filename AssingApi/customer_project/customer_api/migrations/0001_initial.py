# Generated by Django 4.2.1 on 2023-12-27 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=255)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_api.customer')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_api.purchaseorder')),
            ],
        ),
    ]
