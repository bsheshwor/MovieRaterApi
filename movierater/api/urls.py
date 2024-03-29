
from django.urls import path,include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
