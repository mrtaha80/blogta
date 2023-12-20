from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_approved']
    list_filter = ['is_staff', 'is_approved']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['date_joined', 'last_login']

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.is_staff and not request.user.has_perm('users.can_access_admin'):
            return list(self.readonly_fields) + ['is_approved']
        return self.readonly_fields

admin.site.register(CustomUser, CustomUserAdmin)