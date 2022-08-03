from django.db import models


class recipe(models.Model):
    # primary key - named id - auto-generated
    name = models.CharField(max_length=255)
    time = models.PositiveSmallIntegerField()
    link = models.CharField(max_length=2083, default="") # external recipe URL
    thumbnail = models.CharField(max_length=2083, blank=True) # for image URL
    course = models.CharField(max_length=255) # e.g. appetizer, main, dessert
    cuisine = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ingredient(models.Model):
    # primary key used to make connection with recipe
    # via connection to recipe_component jointable
    ingredient_id = models.ManyToManyField(recipe,through='recipe_component')
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255) # e.g. fruit, vegetable, starch
    used_how = models.CharField(max_length=255) # e.g. raw, cooked, baked

    def __str__(self):
        return self.name

class recipe_component(models.Model):
    recipe_component_id = models.IntegerField(primary_key=True)
    # recipe foreign key - id
    recipe_id = models.ForeignKey(
        recipe,on_delete=models.CASCADE, db_column = 'recipe_id') 
    # ingredient foreign key - ingredient_id
    ingredient_id = models.ForeignKey(
        ingredient,on_delete=models.CASCADE, db_column = 'ingredient_id')