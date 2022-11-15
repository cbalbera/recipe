from curses.ascii import isalnum
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

'''class Tag(models.Model):
    TAG_CHOICES = (
        ('light','Light'),
        ('healthy','Healthy'),
        ('hearty', 'Hearty'),
        ('comfort food', 'Comfort Food'),
        ('complex', 'Complex'),
        ('cold weather', 'Cold Weather'),
        ('refreshing', 'Refreshing'),
        ('salad', 'Salad'),
        ('soup', 'Soup'),
        ('stew', 'Stew'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('kosher', 'Kosher'),
        ('dairy-free', 'Dairy-free'),
        ('gluten-free', 'Gluten-free')
    )
    #TODO: 1) selection of these does not appear to work
    #TODO: 2) get all of these to automatically show in admin (and, later, user recipe add)
    #TODO: 3) Shows recipe_app.Tag.None if no tags - fix

    name = models.CharField(max_length=20,choices=TAG_CHOICES, unique=True)

    def __str__(self):
        return self.name
'''

TAGS = (
    ('li','Light'),
    ('he','Healthy'),
    ('ht', 'Hearty'),
    ('cf', 'Comfort Food'),
    ('cx', 'Complex'),
    ('cw', 'Cold Weather'),
    ('rf', 'Refreshing'),
    ('sl', 'Salad'),
    ('so', 'Soup'),
    ('st', 'Stew'),
    ('ve', 'Vegetarian'),
    ('vg', 'Vegan'),
    ('ko', 'Kosher'),
    ('df', 'Dairy-free'),
    ('gf', 'Gluten-free'),
    ('sp', 'Spicy')
)

# having both of these feels unnecessary, but the dict here speeds lookup time in an already-slow function. would be O([# tags this recipe * 3] * [# tags total])
tag_dict = {
    'li':'Light',
    'he':'Healthy',
    'ht': 'Hearty',
    'cf': 'Comfort Food',
    'cx': 'Complex',
    'cw': 'Cold Weather',
    'rf': 'Refreshing',
    'sl': 'Salad',
    'so': 'Soup',
    'st': 'Stew',
    've': 'Vegetarian',
    'vg': 'Vegan',
    'ko': 'Kosher',
    'df': 'Dairy-free',
    'gf': 'Gluten-free'
    }

class recipe(models.Model):

    # enums: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
    #TODO: for each of the below enums, add query parameter validation in views.py
    class Difficulty(models.TextChoices):
        EASY = 'EA', _('Easy')
        MEDIUM = 'MD', _('Medium')
        HARD = 'HA', _('Hard')
        
    def getDifficulty(self):
            # Get value from choices enum
            return self.Difficulty(self.difficulty).label

    class Course(models.TextChoices):
        APPETIZER = 'AP', _('Appetizer')
        MAIN = 'MC', _('Main')
        DESSERT = 'DS', _('Dessert')
        SIDE = 'SD', _('Side')
        TOPPING = 'TO', _('Topping')
        BREAKFAST = 'BK', _('Breakfast')
        
    def getCourse(self):
            return self.Course(self.course).label
    
    class Cuisine(models.TextChoices):
        AMERICAN = 'AM', _('American')
        ITALIAN = 'IT', _('Italian')
        MEDITERRANEAN = 'MD', _('Mediterranean')
        FRENCH = 'FR', _('French')
        CHINESE = 'CH', _('Chinese')
        JAPANESE = 'JP', _('Japanee')
        KOREAN = 'KO', _('Korean')
        VIETNAMESE = 'VT', _('Vietnamese')
        THAI = 'TH', _('Thai')
        MEXICAN = 'MX', _('Mexican')
        INDIAN = 'IN', _('Indian')
        MIDDLE_EASTERN = 'ME', _('Middle Eastern')
        SPANISH = 'SP', _('Spanish')
        ENGLISH = 'EN', _('English')
        GERMAN = 'DE', _('German')
        EASTERN_EUROPEAN = 'EE', _('Eastern European')
        LATIN_AMERICAN = 'LA', _('Latin American')
        AFRICAN = 'AF', _('African')
        INDONESIAN = 'IA', _('Indonesian')
        CARIBBEAN = 'CB', _('Caribbean')
    
    def getCuisine(self):
            return self.Cuisine(self.cuisine).label

    class cookType(models.TextChoices):
        MIX = 'MI', _('Mix / No Cook')
        BAKE = 'BK', _('Bake')
        BOIL = 'BO', _('Boil')
        PAN_SEAR = 'PS', _('Pan Sear')
        PAN_FRY = 'FP', _('Pan Fry')
        STEAM = 'ST', _('Steam')
        DEEP_FRY = 'FD', _('Deep Fry')
        BRAISE = 'BE', ('Braise')
        BROIL = 'BR', _('Broil')
        ROAST = 'RO', _('Roast')

    # primary key - named id - auto-generated
    name = models.CharField(max_length=255)
    time = models.PositiveSmallIntegerField()
    link = models.CharField(max_length=2083, default="") # external recipe URL
    thumbnail = models.CharField(max_length=2083, blank=True) # for image URL
    course = models.CharField(
        max_length = 2,
        choices = Course.choices,
        #, default=[one of the choices]
    )
    cuisine = models.CharField(
        max_length = 2,
        choices = Cuisine.choices
    )
    difficulty = models.CharField(
        max_length = 2,
        choices = Difficulty.choices
    )

    #tags = models.ManyToManyField(Tag)
    tags = models.CharField(max_length = 255)

    def getTags(self):
        tags = []
        # exists in DB as a string, parse and then find tags
        currentString = ''
        for i in range(0,len(self.tags)):
            character = self.tags[i]
            if not character.isalpha():
                if len(currentString) > 0:
                    tags.append(tag_dict.get(currentString))
                currentString = ''
            else:
                currentString = currentString + character
        return tags
    
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