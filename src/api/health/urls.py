from django.urls import include, path
from rest_framework import routers

from .views import HealthCheckViewSet

router = routers.DefaultRouter()
router.register("", HealthCheckViewSet, basename="")

urlpatterns = [
    path("", include(router.urls)),
]
