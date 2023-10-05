from django.db import models

class Customers(models.Model):
    location = models.CharField(max_length=100)
    plan = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(null=True)