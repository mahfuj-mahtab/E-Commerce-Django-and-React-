from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    description = models.CharField(max_length=3000)
    def __str__(self) -> str:
        return self.name