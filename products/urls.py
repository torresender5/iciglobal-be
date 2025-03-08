from django.contrib import admin
from django.urls import path
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls

urlpatterns += [
    # path('suppliers', Suppliers.as_view(), name='suppliers'),
]
