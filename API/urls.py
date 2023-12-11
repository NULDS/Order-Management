from django.urls import path
from .views import  *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', OrderListCreateView.as_view(), name='order-lc'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-rud'),
]
