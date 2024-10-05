from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, CollectionViewSet

router = DefaultRouter()
router.register(r'links', LinkViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]