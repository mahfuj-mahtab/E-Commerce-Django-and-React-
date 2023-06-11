from django.db import models
from api.category.models import Category
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    aditional_image_1 = models.ImageField(upload_to="media",default="none")
    aditional_image_2 = models.ImageField(upload_to="media",default="none")
    aditional_image_3 = models.ImageField(upload_to="media",default="none")
    description = models.CharField(max_length=3000)
    price = models.FloatField(default=0,null=True)
    short_description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name