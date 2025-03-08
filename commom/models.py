from django.db import models

# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class ActiveModel(models.Model):
    active = models.BooleanField(default=True) 

    class Meta:
        abstract = True


class DocumentType(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    document_type_description = models.CharField(max_length=255)
    document_type_code = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
    
    def __str__(self) -> str:
        return  f'{self.document_type_description}'


class PersonInCharge(TimestampedModel, ActiveModel):
    id = models.AutoField(primary_key=True)
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
        verbose_name = 'Persona Responsable'
        verbose_name_plural = 'Personas Responsables'

    def __str__(self) -> str:
        return  f"{self.first_name if self.first_name else ''} { self.last_name if self.last_name else ''}"