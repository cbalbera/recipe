from django.contrib import admin

from .models import *
from .forms import *

# only one of these must be available for use at any time

"""
# recipe admin
class appAdmin(admin.ModelAdmin):

    list_display = ("name", "cuisine",)

admin.site.register(recipe,appAdmin)
"""

# ingredient admin
class appAdmin(admin.ModelAdmin):

    list_display = ("name", "category",)

admin.site.register(ingredient,appAdmin)

"""
class appAdmin(admin.ModelAdmin):

    list_display = ("recipe_name", "ingredient_name",)

admin.site.register(recipe_component,appAdmin)
"""

@admin.register(recipe)    
class RecipeAdmin(admin.ModelAdmin):
    form = recipeAdminForm

'''
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
'''