# Generated by Django 4.2.5 on 2023-10-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_customers_location_alter_customers_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otion', models.CharField(max_length=300)),
            ],
        ),
    ]
