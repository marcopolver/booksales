from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name', 'major')

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@studenti.unibg.it'):
            raise forms.ValidationError('An email from UniBG is required')
        return email

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username', 'email')