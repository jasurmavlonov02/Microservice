from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from Service.models import Category, Service, GroupService


# Register your models here.
class GroupServiceStackedInline(SortableTabularInline):
    model = GroupService
    extra = 1


class ServiceStackedInline(SortableTabularInline):
    model = Service
    extra = 1


class ServiceResource(ModelResource):
    class Meta:
        model = Service


class ServiceNameResource(ModelResource):
    class Meta:
        model = Service
        fields = ["id", "name"]
        name = "Export/Import only service names"


class GroupResource(ModelResource):
    class Meta:
        model = GroupService


class GroupNameResource(ModelResource):
    class Meta:
        model = GroupService
        fields = ["id", "name"]
        name = "Export/Import only group names"


class CategoryResource(ModelResource):
    class Meta:
        model = Category


class CategoryNameResource(ModelResource):
    class Meta:
        model = Category
        fields = ["id", "name"]
        name = "Export/Import only group names"


class CategoryAdmin(SortableAdminMixin, ImportExportModelAdmin):
    ordering = ["order", ]
    search_fields = ["title", ]
    list_display = ['title', 'order', ]
    inlines = [GroupServiceStackedInline, ]
    resource_classes = [CategoryResource, CategoryNameResource]


class GroupServiceAdmin(SortableAdminMixin, ImportExportModelAdmin, ):
    search_fields = ["name"]
    list_filter = ['category', ]
    list_display = ['name', 'my_order']

    inlines = [ServiceStackedInline, ]
    resource_classes = [GroupResource, GroupNameResource]

    class Meta:
        model = GroupService


class ServiceAdmin(ImportExportModelAdmin):
    search_fields = ["group__name", ]
    list_filter = ['group', ]
    list_display = ['name', 'url', 'icon', 'group']
    resource_classes = [ServiceResource, ServiceNameResource]


admin.site.register(Category, CategoryAdmin)
admin.site.register(GroupService, GroupServiceAdmin)
admin.site.register(Service, ServiceAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
