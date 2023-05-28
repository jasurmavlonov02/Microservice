from django.contrib import admin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin

from Service.models import Category, Service, GroupService
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline


#


# Register your models here.
class GroupServiceTabularInline(SortableTabularInline):
    model = GroupService
    extra = 1


class ServiceStackedInline(SortableTabularInline):
    model = Service
    extra = 1


class CategoryAdmin(SortableAdminMixin, ImportExportModelAdmin):
    ordering = ["order", ]
    search_fields = ["title", ]
    list_display = ['title', 'order', ]
    inlines = [GroupServiceTabularInline, ]


class GroupServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ['category', ]
    list_display = ['name', ]

    class Meta:
        model = GroupService


class ServiceAdmin(ImportExportModelAdmin):
    # search_fields = ["", ]
    list_filter = ["groupservice__name"]
    list_display = ['name', 'url', 'icon', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(GroupService, GroupServiceAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.unregister(Group)
