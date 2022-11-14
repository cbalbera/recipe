from django import forms
from django.contrib import admin
from .models import *

class recipeAdminForm(forms.ModelForm):
    tags = forms.MultipleChoiceField(choices = TAGS)

    class Meta:
        model = recipe
        fields = '__all__' # potentially alter going fwd

    def get_clean_tags(self):
        tags = self.cleaned_data['tags']
        print(tags)

        #Validations - TODO customize
        if not tags:
            raise forms.ValidationError("...")

        if len(tags) > 2:
            raise forms.ValidationError("...")
        
        tags = ''.join(tags)
        return tags

'''
class RecipeForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects, widget=forms.SelectMultiple(), required=False)
'''

# https://stackoverflow.com/questions/3582544/django-model-choice-option-as-a-multi-select-box
# https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#selectmultiple