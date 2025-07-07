from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from accounts.serializers import RegisterSerializer
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import RegisterForm


User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProfileView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email
        })
