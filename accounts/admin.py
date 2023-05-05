from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from registration.models import RegistrationProfile as AccountActivation
from registration.admin import RegistrationAdmin as BaseAccountActivationAdmin
from . import models


admin.site.unregister(AccountActivation)


@admin.register(models.AccountActivation)
class AccountActivationAdmin(BaseAccountActivationAdmin):
    pass


# Register your models here.
@admin.register(get_user_model())
class UserAdmin(DjangoUserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name","avatar")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "name", "is_staff", "is_superuser", "is_active", 'date_joined')
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "name")
    ordering = ("-date_joined",)
