from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from recipe_app.models import recipe, ingredient, recipe_component

# Create your views here.

# mapped to URL '/hello'
def say_hello(request):
    return render(request, 'hello.html',{"name":"caleb"})

# mapped to /home
class HomePageView(TemplateView):
    template_name = 'home.html'

# mapped to /search
class SearchResultsView(ListView):
    model = recipe
    template_name = 'search_results.html'
    def get_queryset(self):
        name_query = self.request.GET.get("name")
        print("name is "+name_query)
        cuisine_query = self.request.GET.get("cuisine")
        print("cuisine is "+cuisine_query)
        course_query = self.request.GET.get("course")
        print("course is "+course_query)
        ing_query = self.request.GET.get("ingredient")
        #TODO: update to skip if empty
        ingredient_id = ingredient.objects.filter(Q(name__icontains=ing_query)).values('id')
        print(ingredient_id)
        testq = recipe_component.objects.filter(
            Q(recipe_id=3)
        )
        print(testq)

        # create object list using case-insensitive lookups
        # https://docs.djangoproject.com/en/4.0/topics/db/queries/

        #TODO: update so that fields with no input are ignored, rather than returning all
        object_list = recipe.objects.filter(Q(name__icontains=name_query)
        | Q(cuisine__icontains=cuisine_query)
        | Q(course__icontains=course_query))
        #| Q(recipe_component__ingredient_id__icontains=ingredient_id)
        #)

        return object_list