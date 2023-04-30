import filters
import django_filters

from .models import Dish, Ingredients

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients']
        


