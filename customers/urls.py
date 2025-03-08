from django.contrib import admin
from django.urls import path
from .views import PersonCustomerViewSet, CompanyCustomerViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'persons', PersonCustomerViewSet, basename='persons')
router.register(r'companies', CompanyCustomerViewSet, basename='company')
urlpatterns = router.urls

urlpatterns += [
    # path('suppliers', Suppliers.as_view(), name='suppliers'),
]