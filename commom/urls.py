from django.contrib import admin
from django.urls import path
from .views import DocumentTypeViewSet, PersonInChargeViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'document_type', DocumentTypeViewSet, basename='document_types')
router.register(r'person_in_charge', PersonInChargeViewSet, basename='persons_in_charge')
urlpatterns = router.urls

urlpatterns += [
    # path('suppliers', Suppliers.as_view(), name='suppliers'),
]
