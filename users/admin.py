from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Role


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "is_staff", "is_active", "role")
    list_filter = ("role",)
    fieldsets = (
        (None,
         {
             "fields": ("username", "password", "image", "role")
         }
         ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )

    search_fields = ("username",)
    ordering = ("username",)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Role, RoleAdmin)

admin.site.register(CustomUser, CustomUserAdmin)
