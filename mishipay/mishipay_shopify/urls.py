from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_home, name='home'),
    path('place_order/', views.orders, name='place_order'),
    path('update/<str:order_type>', views.inventory_update, name='inventory_update')
]