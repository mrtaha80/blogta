from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomUser

class CustomUserManagerView:
    def create_user(self, request):
        if request.method == 'POST':
            user = CustomUser.objects.create_user(
                email=request.POST['email'],
                password=request.POST['password']
            )
            user.send_confirmation_email()
            return HttpResponse('User Created', status=201)
        return render(request, 'register.html')

    def create_superuser(self, request):
        if request.method == 'POST':
            user = CustomUser.objects.create_superuser(
                email=request.POST['email'],
                password=request.POST['password']
            )
            user.send_confirmation_email()
            return HttpResponse('Superuser Created', status=201)
        return render(request, 'register.html')