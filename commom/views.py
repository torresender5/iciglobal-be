from django.shortcuts import render

from commom.models import DocumentType, PersonInCharge
from commom.serializers import DocumentTypeSerializer, PersonInChargeSerializer
from rest_framework import viewsets

# Create your views here.



class DocumentTypeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DocumentTypeSerializer
    queryset = DocumentType.objects.all()


class PersonInChargeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PersonInChargeSerializer
    queryset = PersonInCharge.objects.all()