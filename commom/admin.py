from django.contrib import admin

from commom.models import DocumentType, PersonInCharge

# Register your models here.


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('document_type_id', 'document_type_description', 'document_type_code')
    list_filter = ('document_type_id', 'document_type_description', 'document_type_code')
    search_fields = ('document_type_id', 'document_type_description', 'document_type_code')


@admin.register(PersonInCharge)
class PersonInChargeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name'  ,
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',)
    list_filter = (
        'first_name'  ,
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',)
    search_fields = (
        'first_name'  ,
        'second_name',
        'last_name',
        'second_last_name',
        'document_number',
        'document_type',
        'address',
        'phone_number',
        'email',)