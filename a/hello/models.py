from django.db import models

class Customers(models.Model):
    location = models.CharField(max_length=100, null=True)
    plan = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(null=True)

class Success(models.Model):
    otion = models.CharField(max_length=300)

    def __str__(self):
        return self.otion