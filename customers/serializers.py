from commom.serializers import PersonInChargeSerializer
from customers.models import CustomerPerson, customerCompany
from rest_framework import serializers


class CustomerPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerPerson
        fields = '__all__'


class CustomerCompanySerializer(serializers.ModelSerializer):
    person_in_charge = PersonInChargeSerializer()
    class Meta:
        model = customerCompany
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