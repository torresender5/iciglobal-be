
from commom.serializers import PersonInChargeSerializer
from rest_framework import serializers
from supplier.models import SupplierPerson, SupplierCompany


class SuppliersCompanySerializer(serializers.ModelSerializer):
    person_in_charge = PersonInChargeSerializer()
    class Meta:
        model = SupplierCompany
        fields = (
            'id',
            'code',
            'company_name',
            'document_number',
            'document_type',
            'address',
            'phone_number',
            'email',
            'person_in_charge',)

class SuppliersPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SupplierPerson
        fields = '__all__'