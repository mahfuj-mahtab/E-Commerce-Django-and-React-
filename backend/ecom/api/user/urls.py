from django.urls import include,path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('',UserViewSet)

urlpatterns = [
    path('signin/',signin,name = "signin route"),
    path('signout/<int:id>/',signout,name = "signout route"),
    path('',include(router.urls)),
]