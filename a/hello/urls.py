from django.urls import path
from .views import index, get_key, instruction

urlpatterns = [
    path('', index, name='index'),
    path('get_key/', get_key, name='get_key'),
    path('get_key/instruction/', instruction, name='instruction')
]