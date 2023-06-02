from django.contrib import admin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin

from Service.models import Category, Service, GroupService
from adminsortable2.admin import SortableAdminMixin


# Register your models here.


class CategoryAdmin(SortableAdminMixin, ImportExportModelAdmin):
    ordering = ["order", ]
    search_fields = ["title", ]
    list_display = ['title', 'order', ]


class GroupServiceAdmin(SortableAdminMixin, ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["name", ]
    list_filter = ['category', ]
    list_display = ['name', "my_order"]
    ordering = ["my_order", ]

    class Meta:
        model = GroupService


class ServiceAdmin(ImportExportModelAdmin):
    search_fields = ["name", ]
    list_filter = ["groupservice__name"]
    list_display = ['name', 'url', 'icon', ]
    list_per_page = 15


admin.site.register(Category, CategoryAdmin)
admin.site.register(GroupService, GroupServiceAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.unregister(Group)
