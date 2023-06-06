from django.urls import path
from django.contrib.auth.views import LogoutView
from Service.views.auth import login_page, logout
from Service.views.views_api import GroupServiceView
from Service.views.views_jinja import index, search
from config import settings

urlpatterns = [
    # path('category-api/', CategoryList.as_view()),
    # path('group-api/<int:category_id>', GroupServiceView.as_view()),
    # path('category/<int:category_id>/', category, name='category'),
    # path('group/<int:category_id>/', group_service, name='group_service'),
    path('', index, name='index'),
    path('login-page/', login_page, name='login_page'),
    path('search/', search, name='search'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout_page')
]
