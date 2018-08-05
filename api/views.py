# Your imports should be here
from django.shortcuts import render 
from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestListSerializers

# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestListSerializers