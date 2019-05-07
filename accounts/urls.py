# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('<str:username>', views.first_page),
    path('signup/', views.signup, name='signup'),
]