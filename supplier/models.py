from django.db import models

from commom.models import TimestampedModel, ActiveModel, DocumentType, PersonInCharge

# Create your models here.


class SupplierPerson(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    second_name =models.CharField(max_length=50, null=True)
    last_name= models.CharField(max_length=50, null=True)
    second_last_name = models.CharField(max_length=50, null=True)
    document_number = models.CharField(max_length=20, null=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)
    class Meta:
        verbose_name = 'Persona del Proveedor'
        verbose_name_plural = 'Personas de Proveedores'


class SupplierCompany(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=100, null=True)
    document_number = models.CharField(max_length=20, null=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=200, null=True)
    person_in_charge = models.ForeignKey(PersonInCharge, on_delete=models.DO_NOTHING, blank=True, null=True)
    class Meta:
        verbose_name = 'Empresa Proveedor'
        verbose_name_plural = 'Empresas Proveedores'

