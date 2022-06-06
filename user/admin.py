from django.contrib import admin
from .models import CustomUsers
from .forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUsers
    add_form = CustomUserForm
    fieldsets = (*UserAdmin.fieldsets,
                     (
                         'user photo',
                         {
                             'fields':('user_photo',)
                         }
                     )
                 )

admin.site.register(CustomUsers,CustomUserAdmin)