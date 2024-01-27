from django.urls import path
from . import views


urlpatterns = [
    path('product-recipes/<int:product_id>', views.show_recipes_without_product, name='show_recipes'),
    path('add-product-to-recipe/<int:recipe_id>/<int:product_id>/<int:weight>', views.add_product_to_recipe, name='add_product_to_recipe'),
    path('cook-recipe/<int:recipe_id>', views.cook_recipe, name='cook_recipe')
]