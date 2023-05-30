from django.shortcuts import render
from django.db.models import Q, Count
from Service.models import Category


def index(request):
    categories = Category.objects.annotate(num_services=Count('groups__service')).filter(
        Q(num_services__gt=0) | Q(num_services=None)).prefetch_related('groups__service').order_by('order')

    context = {
        'categories': categories,
    }

    return render(request, template_name='service/microservice/index.html', context=context)
