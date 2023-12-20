from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.update({"is_staff": True, "is_superuser": True, "is_approved": True})
        return self.create_user(email, password, **extra_fields)

    def send_confirmation_email(self, user):
        subject = 'تایید ایمیل'
        message = f'لینک تایید: {settings.DOMAIN}'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])