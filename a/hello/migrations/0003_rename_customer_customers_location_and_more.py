# Generated by Django 4.2.5 on 2023-10-04 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_rename_employee_customers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='customer',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='customers',
            old_name='plan_period',
            new_name='plan',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='plan_country',
        ),
    ]