from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

router = DefaultRouter()
router.register("", CarViewSet, basename="car")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cars"
