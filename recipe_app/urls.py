from django.urls import path
from . import views
from .views import AddRecipeView, HomePageView, SearchResultsView
from django.conf.urls.static import static
from django.conf import settings


# URL configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("add/", AddRecipeView.as_view(), name="add_recipe"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 