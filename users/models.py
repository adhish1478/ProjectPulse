from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password= None, role='contibutor', **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email= self.normalize_email(email)
        user= self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, role='admin', **extra_fields)


class CustomUser(AbstractUser):
    username =None
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('contributor', 'Contributor'),
        ('admin', 'Admin')
    )

    email= models.EmailField(unique=True)
    role= models.CharField(max_length=20, choices= ROLE_CHOICES, default='contributor')

    objects= CustomUserManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name= 'User'
        verbose_name_plural= 'Users'
        ordering= ['-date_joined']
