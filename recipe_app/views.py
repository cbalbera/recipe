from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from recipe_app.models import recipe

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
        print("course is is "+course_query)
        object_list = recipe.objects.filter(Q(name__icontains=name_query)
        ).filter(Q(cuisine__icontains=cuisine_query)
        ).filter(Q(course__icontains=course_query))
        return object_list