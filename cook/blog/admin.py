from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Comment)
admin.site.register(DeyWeek)

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


class PostInline(admin.StackedInline):
    model = Menu
    extra = 1

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredients']
    list_filter = ['name', 'ingredients']
    


@admin.register(DishWeek)
class DishWeekAdmin(admin.ModelAdmin):
    list_display = ['dish', 'ingredients', 'dey_week']
    list_filter = ['dish', 'ingredients', 'dey_week']
    




@admin.register(Menu)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'id']
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'menu']






@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['name']
