from django.db import models

from commom.models import TimestampedModel, ActiveModel
from supplier.models import SupplierCompany, SupplierPerson

# Create your models here.


class ProductCategory(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
    unique_name = models.CharField(max_length=20, null=True, unique=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self) -> str:
        return f"{self.unique_name}"


class ProductType(models.Model):
    unique_name = models.CharField(max_length=20, null=True,  unique=True)
    description = models.CharField(max_length=100, null=True)
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
    def __str__(self) -> str:
        return f"{self.unique_name}"
    

class Products(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, null=True,  unique=True)
    # Información básica del producto
    name = models.CharField(max_length=100, null=True)  # Nombre del producto
    description = models.TextField(blank=True)  # Descripción del producto
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Precio del producto
    stock = models.PositiveIntegerField(default=0)  # Cantidad en stock
    sku = models.CharField(max_length=50, unique=True, null=True)  # Código de referencia del producto (SKU)
    # Información adicional
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)  # Relación con la categoría
    
    # Opciones adicionales
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Imagen del producto
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Peso del producto
    dimensions = models.CharField(max_length=100, blank=True)  # Dimensiones del producto (LxAxH)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f"{self.code} {self.name}"
    

class ProductsFromSuppliers(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING, null=True)
    supplier_company = models.ForeignKey(SupplierCompany, on_delete=models.DO_NOTHING, related_name='products_company', null=True)
    supplier_person = models.ForeignKey(SupplierPerson, on_delete=models.DO_NOTHING, related_name='products_person', null=True)

    class Meta:
        verbose_name = 'Product from Supplier'
        verbose_name_plural = 'Products from Suppliers'
    
    def __str__(self) -> str:
        return f"{self.product} {self.supplier_company if self.supplier_company else ''} { self.supplier_person if self.supplier_person else ''}"