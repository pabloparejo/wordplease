#encoding:UTF-8
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic import FormView

from forms import SignUpForm

class LoginView(FormView):
    template_name = "users/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username", "")
        password = form.cleaned_data.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            django_login(self.request, user)

        return redirect("home")




def logout(request):
    django_logout(request)
    return redirect("home")


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

        return redirect("home")
