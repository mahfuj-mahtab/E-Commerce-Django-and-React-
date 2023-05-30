from django.urls import include,path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('',CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]