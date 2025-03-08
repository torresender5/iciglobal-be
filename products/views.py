from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    # def create(self, resquest, *args, **kwarg):
    #     try:
    #         data = resquest.data
    #         document_type_code = data.get('document_type_code')
    #         documen_type = DocumentType.objects.filter(
    #             document_type_code=document_type_code).first()
    #         data.update(document_type=documen_type.document_type_id)
    #         serializer = self.get_serializer(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         return Response({'object': serializer.data}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print('#### ERROR #####', e)
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)