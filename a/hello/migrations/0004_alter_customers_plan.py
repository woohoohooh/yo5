# Generated by Django 4.2.5 on 2023-10-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_rename_customer_customers_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='plan',
            field=models.CharField(max_length=100),
        ),
    ]
