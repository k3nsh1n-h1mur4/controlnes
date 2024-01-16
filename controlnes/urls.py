
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
]
