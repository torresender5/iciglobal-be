from django.contrib import admin

from products.models import ProductCategory, ProductType, Products, ProductsFromSuppliers

# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'unique_name' ,
        'description'
    )
    list_filter = (
        'unique_name' ,
        'description'
    )
    search_fields = (
        'unique_name' ,
        'description'
    )


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'unique_name' ,
        'description'
    )
    list_filter = (
        'unique_name' ,
        'description'
    )
    search_fields = (
        'unique_name' ,
        'description'
    )


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'name',
        'description',
        'product_type',
    )
    list_filter =(
        'code',
        'name',
        'description',
    )
    search_fields=(
        'code',
        'name',
        'description',
    )
@admin.register(ProductsFromSuppliers)
class ProductsFromSuppliersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'supplier_company',
        'supplier_person',
    )
    list_filter = (
        'product',
        'supplier_company',
        'supplier_person',
    )
    search_fields = (
        'product',
        'supplier_company__company_name',
        'supplier_person__first_name',
        'supplier_person__second_name',
        'supplier_person__last_name',
        'supplier_person__second_last_name',
    )


