from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

nested_router = NestedDefaultRouter(router, r'products', lookup='product')
nested_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + nested_router.urls
