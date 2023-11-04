from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    if request.method == 'GET':
        name=request.GET.get('name')
        print(name)
    return HttpResponse(f"Salom {name}")