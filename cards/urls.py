from django.urls import include, path
from rest_framework import routers

from .views import CardViewSet

# Router provides router for standard CRUD functionality
router = routers.DefaultRouter()
router.register(r'', CardViewSet, basename='card')

urlpatterns = [
    path('cards/', include(router.urls))
]
