from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
    'id', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )

    """
    add_fieldsets class variable is used to define the fields that will be displayed on the create user page.

    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'first_name', 'last_name', 'company_name', 'password1', 'password2', 'is_staff',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('id',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)