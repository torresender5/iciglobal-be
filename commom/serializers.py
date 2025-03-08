
from rest_framework import serializers
from .models import DocumentType, PersonInCharge

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('document_type_id', 'document_type_code', 'document_type_description')


class PersonInChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInCharge
        fields = '__all__'