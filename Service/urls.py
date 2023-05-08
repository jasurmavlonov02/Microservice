from django.urls import path

from Service.views.views_api import CategoryList, GroupServiceView
from Service.views.views_jinja import index
urlpatterns = [
    # path('category-api/', CategoryList.as_view()),
    path('group-api/<int:category_id>', GroupServiceView.as_view()),
    # path('category/<int:category_id>/', category, name='category'),
    # path('group/<int:category_id>/', group_service, name='group_service'),
    path('index/', index, name='index')
]

