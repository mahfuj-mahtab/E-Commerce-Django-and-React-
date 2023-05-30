from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return JsonResponse({"Hello" : "hellloo"})