from django.db.models import Prefetch
from django.db.models import Q, Count
from django.shortcuts import render, redirect

from Service.models import Category, GroupService, Service


def index(request):
    if request.user.is_authenticated:
        categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
            Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user))).order_by('order',
                                                                                                 '-is_default', )
    else:
        categories = Category.objects.filter(is_default=True)

    context = {
        'categories': categories,
    }

    return render(request, template_name='service/microservice/index.html', context=context)


def search(request):
    search_query = request.GET.get('q', None)
    if request.user.is_authenticated:

        if search_query:
            categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
                Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user)) & Q(
                    groups__service__name__icontains=search_query)).prefetch_related(
                Prefetch('groups', queryset=GroupService.objects.all().filter(service__name__icontains=search_query)),
                Prefetch('groups__service', queryset=Service.objects.all().filter(name__icontains=search_query)),
            ).order_by('order', '-is_default', )

            if not categories:
                return redirect('not_found')
        else:
            # categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
            #     Q(num_services__gt=0) & (Q(is_default=True) | Q(role__users=request.user))).prefetch_related(
            #     'groups__service').order_by('order', '-is_default', )

            return redirect('not_found')




    else:
        if search_query:
            categories = Category.objects.filter(
                Q(is_default=True) & Q(groups__service__name__icontains=search_query)).prefetch_related(
                Prefetch('groups', queryset=GroupService.objects.all().filter(service__name__icontains=search_query)),
                Prefetch('groups__service', queryset=Service.objects.all().filter(name__icontains=search_query)),
            )
            if not categories:
                return redirect('not_found')
        else:
            categories = Category.objects.filter(is_default=True)

    context = {
        'categories': categories,
    }

    return render(request, template_name='service/microservice/search.html', context=context)


def not_found_view(request):
    return render(request, 'service/microservice/not_found.html')
