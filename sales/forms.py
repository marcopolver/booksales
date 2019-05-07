from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import StudentProfile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@studenti.unibg.it'):
            raise forms.ValidationError('An email from UniBG is required')
        return email

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'surname', 'major']
