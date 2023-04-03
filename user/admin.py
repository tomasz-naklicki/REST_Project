from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "id",
        "username",
        "user_type",
    )
    list_filter = ("username", "user_type", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password", "user_type")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "user_permissions",
                    "user_type",
                ),
            },
        ),
    )

    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
