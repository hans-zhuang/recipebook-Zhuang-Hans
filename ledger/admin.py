from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

# Register your models here.

class RecipeIngredientLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = [RecipeIngredientLine]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)