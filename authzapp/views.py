from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello, worl. you're at the authzapp index")

