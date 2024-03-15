from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Recipe, Ingredient, RecipeIngredient


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientLine(admin.TabularInline):
    model = [RecipeIngredient]


class RecipeAdmin(admin.ModelAdmin):
    model = [RecipeIngredientLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)