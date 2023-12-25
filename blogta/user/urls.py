from django.urls import path
from .views import CustomUserManagerView
from django.contrib.auth.views import LoginView, LogoutView

user_manager = CustomUserManagerView()

urlpatterns = [
    path('create-user/', user_manager.create_user, name='create_user'),
    path('create-superuser/', user_manager.create_superuser, name='create_superuser'),
    path('change-user/<int:pk>/', user_manager.change_user, name='change_user'),
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]



    