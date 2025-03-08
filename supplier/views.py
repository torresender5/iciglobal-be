from django.shortcuts import render
from django.http import JsonResponse
from commom.models import DocumentType, PersonInCharge
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from supplier.models import SupplierCompany, SupplierPerson
from drf_yasg.utils import swagger_auto_schema
# from qr_code.qr_code import make_qr
import qrcode
from io import BytesIO
import base64

from supplier.serializers import SuppliersCompanySerializer, SuppliersPersonSerializer
# Create your views here.


class PersonSuppliers(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]
    queryset = SupplierPerson.objects.all()
    serializer_class = SuppliersPersonSerializer
    
    
    # def list(self, request):
    #     try:
    #         persons = SupplierPerson.objects.all()
    #         data = SuppliersPersonSerializer(persons, many=True).data
            
    #         return Response(data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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

    # def post(self, resquest):
    #     try:
    #         data = resquest.data
    #         documen_type = DocumentType.objects.filter(
    #             document_type_code='identity_card').first()
    #         data.update(document_type=documen_type)
    #         person = SupplierPerson.objects.create(**data)
    #         result = SuppliersPersonSerializer(person)
    #         return Response({'object': result.data}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)
        

class CompanySuppliers(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication] 
    queryset = SupplierCompany.objects.all()
    serializer_class = SuppliersCompanySerializer

    # @swagger_auto_schema(security=[{'Bearer': []}])
    # def list(self, request):
    #     try:
    #         companies = SupplierCompany.objects.all()
    #         data = SuppliersCompanySerializer(companies, many=True).data
    #         # print('desde company suppliers', data)
            
    #         return Response(data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         # print(e)
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
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
            company = SupplierCompany.objects.create(**data)
            result = SuppliersCompanySerializer(company)
            return Response({'object': result.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
class GenerateQR(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        url = request.GET.get('url', 'https://www.ejemplo.com')  # URL por defecto
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        # Guardar la imagen en un buffer
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        # Codificar la imagen en base64
        qr_code_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        return JsonResponse({'qr_code': f'data:image/png;base64,{qr_code_base64}'})