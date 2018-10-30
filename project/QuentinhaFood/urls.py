from django.urls import path, include
from QuentinhaFood import views as my_views

urlpatterns = [
    path('', my_views ,name=''),
]
