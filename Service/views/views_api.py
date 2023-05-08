from rest_framework.generics import ListAPIView

from Service.models import Category, GroupService
from Service.paginations import StandardResultsSetPagination
from Service.serializers import CategorySerializer, GroupServiceSerializer


# Create your views here.

class CategoryList(ListAPIView):
    queryset = Category.objects.all().prefetch_related('groups')
    serializer_class = CategorySerializer


class GroupServiceView(ListAPIView):
    # queryset = MicroService.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = GroupServiceSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return GroupService.objects.filter(category_id=category_id).prefetch_related('services')

#
# class GroupServiceView(GenericAPIView):
#     def get(self, request):
#         cat_id = request.GET.get('id')
#         cat_query = Category.objects.filter(id=cat_id)
#         cat_serializer = CategorySerializer
#
#         group_query = GroupService.objects.filter(category_id=cat_id)
#         group_serializer = GroupServiceSerializer
#
#         serializer1 = cat_serializer(cat_query, many=True)
#         serializer2 = group_serializer(group_query, many=True)
#
#         data = {
#             'data': {
#                 'category': serializer1.data,
#                 'group_service': serializer2.data
#             }
#
#         }
#         return Response(data, status=status.HTTP_200_OK)
#
#
