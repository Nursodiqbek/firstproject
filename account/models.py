from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManage(BaseUserManager):

    def create_user(self,phone,password,**extra_fields):

        if not phone:
            raise ValueError(_("phone required field!"))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,phone,password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)


        if extra_fields.get("is_staff") is not True:

            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)



class CustomUser(AbstractUser):

    MALE = "M"
    FAMALE = "F"


    GENDER = (
        ("M",MALE),
        ("F",FAMALE)
    )
    phone = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=2, choices=GENDER, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManage()

    def __str__(self):
        return self.phone



