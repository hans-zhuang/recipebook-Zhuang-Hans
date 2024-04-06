from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/add_image', RecipeUpdateView.as_view(), name='recipe-image'),
]
app_name = "ledger"