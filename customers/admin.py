from django.contrib import admin

from customers.models import CustomerPerson, customerCompany

# Register your models here.

@admin.register(CustomerPerson)
class SupplierPersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'first_name',
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email')
    
    list_filter = (
        'id',
        'code',
        'first_name',
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email'
    )
    search_fields = (
        'id',
        'code',
        'first_name',
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email'
    )

@admin.register(customerCompany)
class SupplierCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'company_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',
        'person_in_charge',
    )
    
    list_filter = (
        'code',
        'company_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',
    )
    search_fields = (
        'code',
        'company_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',
    )