from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm , CustomUserChangeForm
from .models import CustomUser

class CustomUserManagerView:
    def create_user(self, request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.send_confirmation_email()
                return HttpResponse('User Created', status=201)
        return render(request, 'register.html', {'form': form})

def create_superuser(self, request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                return HttpResponse('Superuser Created', status=201)
        return render(request, 'register.html', {'form': form})
class CustomUserManagerView:
    def change_user(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                return HttpResponse('User Updated', status=200)
        return render(request, 'change_user.html', {'form': form, 'user': user})