from django.contrib import admin
from django.urls import path
from .views import GenerateQR, PersonSuppliers, CompanySuppliers
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'persons', PersonSuppliers, basename='persons')
router.register(r'companies', CompanySuppliers, basename='company')
urlpatterns = router.urls

urlpatterns += [
    # path('suppliers', Suppliers.as_view(), name='suppliers'),
    path('generate_qr/', GenerateQR.as_view(), name='generate_qr')
]
