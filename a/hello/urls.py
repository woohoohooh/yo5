from django.urls import path
from .views import index, check_payment

urlpatterns = [
    path('', index, name='index'),
    path('check_payment/', check_payment, name='check_payment'),
]