from django.contrib import admin
from .models import Post,Comment,User

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CreateUserForm, CustomUserChangeForm
from django.contrib.auth.models import User

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]



