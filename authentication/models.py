from operator import is_
from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import (PermissionsMixin, UserManager,BaseUserManager, AbstractBaseUser)

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.hashers import make_password

class MyUserManager(BaseUserManager):

       
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
                raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

    

class MyUser(PermissionsMixin, AbstractBaseUser, TrackingModel):
   email= models.EmailField(_("email address"), max_length=254, unique=True)
   email_verified= models.BooleanField(_("email verified"), default=False)
   first_name= models.CharField(_("first name"), max_length=255, blank=True)
   last_name= models.CharField(_("last name"), max_length=255, blank=True)
   username= models.CharField(_("username"), max_length=254, unique=True)
   is_active = models.BooleanField(_("active"), default=False)
   is_staff = models.BooleanField(_("staff"), default=False)
      
      
   USERNAME_FIELD = 'email'   
   REQUIRED_FIELDS = ['username']
       
   def __str__(self):
       return self.username    
       
   objects = MyUserManager()   
   @property
   def tokens(self):
        return ""
        