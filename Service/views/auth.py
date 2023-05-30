from django.shortcuts import render


def login_page(request):
    return render(request, template_name='service/microservice/auth.html')
