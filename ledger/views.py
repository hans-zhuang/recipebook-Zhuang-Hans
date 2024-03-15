from .models import RecipeIngredient, Recipe
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


# def recipe_list(request):
#     ctx =  {
#       "recipes": [
#         {
#           "name": "Recipe 1",
#           "ingredients": [
#             {
#               "name": "tomato",
#               "quantity": "3pcs"
#             },
#             {
#               "name": "onion",
#               "quantity": "1pc"
#             },
#             {
#               "name": "pork",
#               "quantity": "1kg"
#             },
#             {
#               "name": "water",
#               "quantity": "1L"
#             },
#             {
#               "name": "sinigang mix",
#               "quantity": "1 packet"
#             }
#             ],
#             "link": "/recipe/1"
#         },
#         {
#           "name": "Recipe 2",
#           "ingredients": [
#               {
#                 "name": "garlic",
#                 "quantity": "1 head"
#               },
#               {
#                 "name": "onion",
#                 "quantity": "1pc"
#               },
#               {
#                 "name": "vinegar",
#                 "quantity": "1/2cup"
#               },
#               {
#                 "name": "water",
#                 "quanity": "1 cup"
#               },
#               {
#                 "name": "salt",
#                 "quantity": "1 tablespoon"
#               },
#               {
#                 "name": "whole black peppers",
#                 "quantity": "1 tablespoon"
#               },
#               {
#                 "name": "pork",
#                 "quantity": "1 kilo"
#               }
#               ],
#               "link": "/recipe/2"
#         }
#         ]
#     }
#     return render(request, "recipe_list.html", ctx)

# def recipe_1(request):
#     ctx = {
#       "name": "Recipe 1",
#       "ingredients": [
#         {
#           "name": "tomato",
#           "quantity": "3pcs"
#         },
#         {
#           "name": "onion",
#           "quantity": "1pc"
#         },
#         {
#           "name": "pork",
#           "quantity": "1kg"
#         },
#         {
#           "name": "water",
#           "quantity": "1L"
#         },
#         {
#           "name": "sinigang mix",
#           "quantity": "1 packet"
#         }
#       ],
#       "link": "/recipe/1"
#     }
#     return render(request, "recipe_1.html", ctx)

# def recipe_2(request):
#     ctx = {
#       "name": "Recipe 2",
#       "ingredients": [
#         {
#           "name": "garlic",
#           "quantity": "1 head"
#         },
#         {
#           "name": "onion",
#           "quantity": "1pc"
#         },
#         {
#           "name": "vinegar",
#           "quantity": "1/2cup"
#         },
#         {
#           "name": "water",
#           "quantity": "1 cup"
#         },
#         {
#           "name": "salt",
#           "quantity": "1 tablespoon"
#         },
#         {
#           "name": "whole black peppers",
#           "quantity": "1 tablespoon"
#         },
#         {
#           "name": "pork",
#           "quantity": "1 kilo"
#         }
#       ],
#       "link": "/recipe/2"
#     }
#     return render(request, "recipe_2.html", ctx)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe 
    template_name = 'recipe_detail.html'
    redirect_field_name = 'recipe_list.html'
    context_object_name = 'recipes'


class recipe_detail(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id).name
        ingredients = RecipeIngredient.objects.filter(recipe__name=recipe)
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'recipe_detail.html', context)