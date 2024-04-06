from .models import RecipeIngredient, Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'login.html'
    context_object_name = 'recipes'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_create.html'


class RecipeUpdateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_update.html'

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_detail = Recipe.objects.get(pk=self.kwargs['pk'])
            recipe = form.save(commit=False)
            recipe.recipe = recipe_detail
            recipe.save()
            return redirect('ledger:recipe_detail', pk=recipe_detail.pk)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class recipe_detail(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id).name
        ingredients = RecipeIngredient.objects.filter(recipe__name=recipe)
        images = RecipeImage.objects.filter(recipe__name=recipe)
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'images': images,
        }
        return render(request, 'recipe_detail.html', context)