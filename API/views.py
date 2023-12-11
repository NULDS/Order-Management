from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_quantity','order_status']


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'product_quantity','order_status']

def home(request):
    return render(request,'orders.html')
