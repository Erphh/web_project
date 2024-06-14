from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_active','is_authenticate')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','otp_secret')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin','is_authenticate')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_admin','is_authenticate'),
        }),
    )

admin.site.register(Account, AccountAdmin)

