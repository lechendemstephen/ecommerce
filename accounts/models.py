from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser # type: ignore
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser): 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=30)

    jioned_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username', 'last_name']
    


    def __str__(self): 
        return self.first_name, self.last_name
    
    def has_perm(self, perms, obj=None): 
        return self.is_admin
    def has_module_perms(self, add_label): 
        return True
    