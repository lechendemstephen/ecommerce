from django.contrib import admin # type: ignore
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin): 
    list_display = ('username', 'email', 'password')


admin.site.register(User, UserAdmin)