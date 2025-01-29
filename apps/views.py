from django.shortcuts import render, redirect
from apps.models import Users
from django.views.generic import CreateView, FormView
from django.views import View
from .forms import UserCreateForm, UserSigninForm
from .mixins import NotLoginRequiredMixin
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token

class UserCreateView(NotLoginRequiredMixin, CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = '/'   

class UserSigninView(FormView):
    form_class = UserSigninForm
    template_name = 'signin.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = Users.objects.filter(username=username).first()
        # print(password, username, user)
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)
    

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
