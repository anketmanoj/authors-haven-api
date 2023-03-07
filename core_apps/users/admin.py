from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['pkid', 'id', 'email', 'username', 'first_name', 'last_name', 'is_staff',]
    list_display_links = ['id', 'email',]
    list_filter = ['email', 'username', 'first_name', 'is_staff',]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                'fields': (
                    'email',
                    'password',
                )
            },
        ),
        (
            _("Personal Info"),
            {
                'fields': (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (
            _("Important Dates"),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                )
            },
        ),
    )
    search_fields = ['email', 'username', 'first_name', 'last_name',]

admin.site.register(User, UserAdmin)
