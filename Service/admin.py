from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from django.contrib import admin

from Service.models import Category, Service, GroupService


# Register your models here.

class GroupServiceStackedInline(SortableTabularInline):
    model = GroupService


class ServiceStackedInline(SortableTabularInline):
    model = Service


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ["order"]
    search_fields = ["title"]
    list_display = ['title', 'order']
    inlines = [GroupServiceStackedInline]


admin.site.register(Category, CategoryAdmin)


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ["group__name", ]
    list_filter = ['group', ]
    list_display = ['name', 'url', 'icon', 'group']


admin.site.register(Service, ServiceAdmin)


class GroupServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ['category', ]
    list_display = ['name', 'my_order']
    inlines = [ServiceStackedInline]


admin.site.register(GroupService, GroupServiceAdmin)
