from django.db import models


class recipe(models.Model):
    name = models.CharField(max_length=255)
    time = models.PositiveSmallIntegerField()
    link = models.CharField(max_length=2083, default="") # external recipe URL
    thumbnail = models.CharField(max_length=2083, blank=True) # for image URL
    course = models.CharField(max_length=255) # e.g. appetizer, main, dessert
    cuisine = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255) # e.g. fruit, vegetable, starch
    used_how = models.CharField(max_length=255) # e.g. raw, cooked, baked

    def __str__(self):
        return self.name

class recipe_component(models.Model):
    recipe_component_id = models.IntegerField(primary_key=True)
    recipe_id = models.IntegerField() # foreign key - id in recipe
    ingredient_id = models.IntegerField() # foreign key - id in ingredient