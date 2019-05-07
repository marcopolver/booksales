from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from sales.forms import CustomUserCreationForm, CustomUserChangeForm
from sales.models import StudentProfile

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = StudentProfile
#     list_display = ['email', 'username', 'name', 'surname', 'major']
admin.site.register(StudentProfile)