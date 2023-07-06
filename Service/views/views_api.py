from django.db.models import Q, Prefetch, Count
from rest_framework.response import Response
from rest_framework.views import APIView

from Service.models import GroupService, Category, Service
from Service.serializers import CategorySerializer
from users.models import CustomUser


# Create your views here.


class CategoryApiView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')

        if request.user.is_authenticated:

            if query:
                categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
                    Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user)) & (Q(
                        groups__service__name__icontains=query) | Q(
                        groups__name__icontains=query))).distinct().prefetch_related(
                    Prefetch('groups',
                             queryset=GroupService.objects.all().filter(Q(
                                 service__name__icontains=query) | Q(name__icontains=query)).distinct()),
                    Prefetch('groups__service',
                             queryset=Service.objects.all().filter(
                                 Q(name__icontains=query) | Q(services__name__icontains=query)).distinct()),
                )



            else:
                categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
                    Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user))).prefetch_related(
                    'groups__service')





        else:
            if query:
                categories = Category.objects.filter(
                    Q(is_default=True) & (Q(groups__service__name__icontains=query) | Q(
                        groups__name__icontains=query))).distinct().prefetch_related(
                    Prefetch('groups',
                             queryset=GroupService.objects.all().filter(Q(
                                 service__name__icontains=query) | Q(name__icontains=query)).distinct()),
                    Prefetch('groups__service',
                             queryset=Service.objects.all().filter(
                                 Q(name__icontains=query) | Q(services__name__icontains=query)).distinct()),
                )

            else:
                categories = Category.objects.filter(is_default=True)

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
