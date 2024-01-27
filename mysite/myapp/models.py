from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    using_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingridients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingridients')
    weight = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.recipe.name} - {self.product} - {self.weight} gr'
    
    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
