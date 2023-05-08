from django.shortcuts import render

from Service.models import Category


def index(request):
    categories = Category.objects.all().prefetch_related('groups__services')

    context = {
        'categories': categories,
    }

    return render(request, template_name='service/microservice/index.html', context=context)
