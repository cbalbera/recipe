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
        object_list = recipe.objects.all()
        name_query = self.request.GET.get("name")
        # create object list using case-insensitive lookups
        # https://docs.djangoproject.com/en/4.0/topics/db/queries/
        if name_query:
            #TODO: add validation
            object_list = object_list.filter(Q(name__icontains=name_query))
            print("name is "+name_query)
        cuisine_query = self.request.GET.get("cuisine")
        if cuisine_query:
            #TODO: add validation
            object_list = object_list.filter(Q(cuisine__icontains=cuisine_query))
            print("cuisine is "+cuisine_query)
        course_query = self.request.GET.get("course")
        if course_query:
            #TODO: add validation
            object_list = object_list.filter(Q(course__icontains=course_query))
            print("course is "+course_query)
        ing_query = self.request.GET.get("ingredient")
        if ing_query:
            #TODO: update to accept multiple inputs
            #TODO: add validation
            object_list = object_list.filter(Q(ingredient__name__icontains=ing_query))
            print("ingredient is "+ing_query)

        return object_list