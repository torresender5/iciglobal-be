from django.contrib import admin

from login.models import User
from django.contrib.auth.models import Permission
# admin.register(Permission)
# @admin.register(Permission)
# @admin.register(Group)
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'second_name',
        'second_last_name',)
    list_filter = (
        'username',
        'first_name',
        'last_name',
        'email',
        'second_name',
        'second_last_name',)
    search_fields =(
        'username',
        'first_name',
        'last_name',
        'email',
        'second_name',
        'second_last_name',)