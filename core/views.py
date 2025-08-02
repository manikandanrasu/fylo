from django.shortcuts import render
from django.http import HttpResponseNotAllowed
import json
import logging

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def generate(request):
    if request.method != ["POST"]:
        return HttpResponseNotAllowed(["POST"])
