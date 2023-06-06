from django.db.models import Prefetch
from django.db.models import Q, Count
from django.shortcuts import render

from Service.models import Category, GroupService, Service
from users.models import CustomUser


def index(request):
    split_full_name = ''
    if request.user.is_authenticated:
        user = CustomUser.objects.filter(id=request.user.id).first()
        split_full_name = user.full_name.split()[0]

        categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
            Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user))).order_by('-is_default',
                                                                                                 'order', )
    else:
        categories = Category.objects.filter(is_default=True).order_by('-is_default', 'order', )

    context = {
        'categories': categories,
        'split_full_name': split_full_name
    }

    return render(request, template_name='service/microservice/index.html', context=context)


def search(request):
    search_query = request.GET.get('q', None)
    split_full_name = ''
    if request.user.is_authenticated:
        user = CustomUser.objects.filter(id=request.user.id).first()
        split_full_name = user.full_name.split()[0]

        if search_query:
            categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
                Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user)) & Q(
                    groups__service__name__icontains=search_query)).prefetch_related(
                Prefetch('groups', queryset=GroupService.objects.all().filter(service__name__icontains=search_query)),
                Prefetch('groups__service', queryset=Service.objects.all().filter(name__icontains=search_query)),
            )



        else:
            categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
                Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user))).prefetch_related(
                'groups__service')





    else:
        if search_query:
            categories = Category.objects.filter(
                Q(is_default=True) & Q(groups__service__name__icontains=search_query)).prefetch_related(
                Prefetch('groups', queryset=GroupService.objects.all().filter(service__name__icontains=search_query)),
                Prefetch('groups__service', queryset=Service.objects.all().filter(name__icontains=search_query)),
            )

        else:
            categories = Category.objects.filter(is_default=True)

    context = {
        'categories': categories,
        'search_query': search_query,
        'split_full_name': split_full_name

    }

    return render(request, template_name='service/microservice/search.html', context=context)
