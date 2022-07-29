from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from recipe_app.models import recipe

# Create your views here.

# mapped to URL '/hello'
def say_hello(request):
    return render(request, 'hello.html',{"name":"caleb"})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = recipe
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = recipe.objects.filter(
            Q(name__icontains=query) | Q(cuisine__icontains=query)
        )
        return object_list