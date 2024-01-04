from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def cards(request):
    return render(request, "cards.html")

def tables(request):
    return render(request, "tables.html")