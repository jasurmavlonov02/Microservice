from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
import requests

from Service.forms import LoginForm
from users.models import CustomUser


# payload = {
#     "username": "jelmurodov",
#     "password": "123qwe!@#"
# }
#
# r = requests.post(url="https://portal.tmart.uz/api/v1/user/auth", json=payload)
# data = r.json()


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            payload = {
                "username": cd["username"],
                "password": cd["password"]
            }

            r = requests.post(url="https://portal.tmart.uz/api/v1/user/auth", json=payload)
            data = r.json()

            if data["success"]:
                if not CustomUser.objects.filter(username=payload["username"]).exists():
                    user = CustomUser.objects.create_user(username=cd["username"], password=cd["password"])
                    user.full_name = data["full_name"]
                    user.phone = data["phone"]
                    user.email = data["email"]
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                    login(request, user)
                    return redirect('index')
                else:
                    user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
                    if user is not None:
                        login(request, user)
                        return redirect('index')
                    else:
                        messages.add_message(
                            request,
                            level=messages.ERROR,
                            message='Неправильный логин или пароль'
                        )
            else:
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message='Неправильный логин или пароль'
                )
    else:
        form = LoginForm()

    return render(request, 'service/microservice/auth.html', {'form': form})
