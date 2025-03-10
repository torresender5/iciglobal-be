"""
URL configuration for ici_global project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ICI GLOBAL API",
        default_version='v1',
        description="ICI GLOBAL API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@miapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
    

urlpatterns += [
    # re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    # path('schema/', get_schema_view(title='API Schema')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('login.urls')),
    path('supplier/', include('supplier.urls')),
    path('commom/', include('commom.urls')),
    path('customers/', include('customers.urls')),
    path('', include('products.urls')),
    
]
