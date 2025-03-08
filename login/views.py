from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer

# Create your views here.


class Protegida(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"content": "Esta vista está protegida"})
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # Llama al método original para obtener el token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Aquí puedes manipular los datos o ejecutar otras funciones
        print('######', serializer.data)
        # user = serializer.validated_data['user']
        # Por ejemplo, puedes registrar el inicio de sesión
        # self.log_user_login(user)

        # Devuelve la respuesta con los tokens
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def log_user_login(self, user):
        # Implementa la lógica que necesites, como registrar el inicio de sesión
        print(f"Usuario {user.username} ha iniciado sesión.")