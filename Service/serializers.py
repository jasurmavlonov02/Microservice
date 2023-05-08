from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Service.models import Category, Service, GroupService


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class GroupServiceSerializer(ModelSerializer):
    services = SerializerMethodField()

    def get_services(self, obj):
        services = obj.services.all()
        return MicroServiceSerializer(services, many=True, context=self.context).data

    class Meta:
        model = GroupService
        fields = ('name', 'services')


class MicroServiceSerializer(ModelSerializer):
    icon = SerializerMethodField()

    def get_icon(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.icon.url)

    class Meta:
        model = Service
        fields = ('name', 'url', 'icon', 'description')
