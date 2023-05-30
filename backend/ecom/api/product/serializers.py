from rest_framework import serializers
from .models import *
class ProductsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        depth = 1
        fields = '__all__'