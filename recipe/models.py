from ctypes import _CArgObject
from django.db import models

class Recipe (models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 200 , blank = False , default = " ")
    details = models.CharField(max_length = 200 , default = " ")
    ingredients = models.CharField(max_length = 200 , blank = False , default = " ")
    image = models.IntegerField()
    recipe_prepration = models.TextField()
    calories = models.IntegerField(null = True)
    protein = models.IntegerField(null = True)
    carbo = models.IntegerField(null = True)
    

    class Meta:
         db_table = 'Recipe'