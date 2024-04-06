from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='A Random Person')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='author',
        default = None
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.id])
    
    def go_back(self):
        return reverse('ledger:recipe_list')
    

class RecipeImage(models.Model):
    Image = models.ImageField(upload_to='images/', null=False)
    Description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images'
    )


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return '{} {}'.format(Ingredient.name, self.quantity)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.id])