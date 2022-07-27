from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# mapped to URL '/hello'
def say_hello(request):
    return render(request, 'hello.html',{"name":"caleb"})