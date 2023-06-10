from django.contrib import admin
from django.urls import path,include
# import api
from .views import *
urlpatterns = [
    path("", Home,name="home"),
    path("category/", include("api.category.urls")),
    path("products/", include("api.product.urls")),
    path("users/", include("api.user.urls")),
]
