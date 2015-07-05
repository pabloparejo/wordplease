#encoding:UTF-8
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.views.generic import View, FormView, ListView

from forms import LoginForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            username = form.cleaned_data.get("username", "")
            password = form.cleaned_data.get("password", "")
            user = authenticate(username=username, password=password)

            if user:
                django_login(request, user)
                url = request.GET.get("next", "login")
                return redirect(url)

            else:
                context["error"] = "Usuario o contraseña incorrectos"

        return render(request, "users/login.html", context)


def logout(request):
    django_logout(request)
    return reverse_lazy("/")


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username", "")
        password = form.cleaned_data.get("password1", "")
        user = authenticate(username=username, password=password)

        django_login(self.request, user)

        return redirect("/")
