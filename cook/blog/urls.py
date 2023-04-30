from django.urls import path
from .views import menu_list_create, menu_update, menu_destroy


urlpatterns = [
    path('menu-list-create/', menu_list_create, name='MenuListCreate'),
    path('menu-update/<int:pk>/', menu_update, name='MenuUpdate'),
    path('menu-destroy/<int:pk>/', menu_destroy, name='MenuDestroy'),
]