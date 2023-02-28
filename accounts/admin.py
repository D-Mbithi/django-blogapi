from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'name', 'email', 'is_staff', 'is_active']

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('name',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('name',)}),)
