
from django.urls import include, path
from .views import GamesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"games", GamesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]