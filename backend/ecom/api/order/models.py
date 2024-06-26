from django.db import models
from api.user.models import CustomUser
from api.product.models import *
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1000)
    total_products = models.CharField(max_length=50,default=0)
    transaction_id = models.CharField(max_length=200,default=0)
    total_amount = models.CharField(max_length=50,default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
