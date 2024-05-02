from django.urls import include,path
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register(r'',ProductsViewSet)
# router.register('single/<int:id>/',SingleProductShow)

urlpatterns = [
    path('',include(router.urls)),
    path('single/<int:id>/',SingleProductShow, name = 'single product show')
]