from django.shortcuts import render
from django.views.generic import ListView


from .models import Menu, Recipe, Category
from .serializers import menu_serializer
# from accounts.permissions import IsAdminPermission
from rest_framework import permissions 
from rest_framework import generics


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menu_serializer
    
menu_list_create = MenuListCreateAPIView.as_view()


class MenuRetriveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menu_serializer
   
menu_update = MenuRetriveUpdate.as_view()


class MenuRetriveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menu_serializer

menu_destroy = MenuRetriveDestroyAPIView.as_view()







