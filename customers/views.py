from django.shortcuts import render
from commom.models import DocumentType, PersonInCharge
from customers.models import CustomerPerson, customerCompany
from customers.serializers import CustomerCompanySerializer, CustomerPersonSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class PersonCustomerViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]
    queryset = CustomerPerson.objects.all()
    serializer_class = CustomerPersonSerializer

    def create(self, resquest, *args, **kwarg):
        try:
            data = resquest.data
            document_type_code = data.get('document_type_code')
            documen_type = DocumentType.objects.filter(
                document_type_code=document_type_code).first()
            data.update(document_type=documen_type.document_type_id)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({'object': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print('#### ERROR #####', e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        

class CompanyCustomerViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication] 
    queryset = customerCompany.objects.all()
    serializer_class = CustomerCompanySerializer
    
    def post(self, resquest):
        try:
            data = resquest.data
            print(data)
            if data.get('person_in_charge'):
                documen_type = DocumentType.objects.filter(
                    document_type_code=data.get('person_in_charge').get('documen_type')).first()
                data['person_in_charge'].update(document_type=documen_type)
                person_in_charge = PersonInCharge.objects.create(**data.get('person_in_charge'))
                print(person_in_charge)
                data.update(person_in_charge=person_in_charge)

            documen_type = DocumentType.objects.filter(
                document_type_code=data.get('documen_type')).first()
            data.update(document_type=documen_type)
            company = customerCompany.objects.create(**data)
            result = CustomerCompanySerializer(company)
            return Response({'object': result.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)