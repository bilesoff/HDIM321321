from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import get_user_model, logout, login as user_login

User = get_user_model()


class RegistrationView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect('catalog_list')
        return render(request, template_name='registration/register.html')

    def post(self, request: HttpRequest):
        login = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(login, email, password)
        user_login(request=request, user=user)

        return redirect('catalog_list')


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect('catalog_list')