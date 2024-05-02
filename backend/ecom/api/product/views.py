from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
 # Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializers
    
def  SingleProductShow(request,id):
    product =  Products.objects.get(id = id)
    serializer = SingleProductsSerializers(product)
    # print(serializer.data, ' product data')
    return JsonResponse(serializer.data, safe= False)
        