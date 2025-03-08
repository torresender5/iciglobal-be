
from django.contrib import admin
from django.urls import path
from .views import CustomTokenObtainPairView, Protegida


    

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('protegida/', Protegida.as_view(), name='login')
]
