from django.shortcuts import render
from itertools import chain
from django.http import HttpResponse
from .models import Product, Recipe, Ingredient


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    product = Product.objects.filter(id=product_id).first()
    ingridient, created = Ingredient.objects.get_or_create(recipe=recipe, product=product)
    ingridient.weight = weight
    ingridient.save()

    return HttpResponse('Продукт добавлен в рецепт')

   
def cook_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    ingridients = recipe.ingridients.all()
    for ingridient in ingridients:
        product = ingridient.product
        product.using_count += 1
        product.save()

    return HttpResponse("Количество использования продукта для приготовления блюдаб изменилось")


def show_recipes_without_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    ingridients_lt_10 = product.ingridients.filter(weight__lt=10)
    ingridients_product_not_used = Ingredient.objects.exclude(product=product)
    ingridients = chain(ingridients_lt_10, ingridients_product_not_used)
    recipes = [ingridient.recipe for ingridient in ingridients]
    context = {
        'recipes': recipes
    }
    return render(request, 'home/index.html', context)
