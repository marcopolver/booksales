from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class GenericUser(models.Model):
    username = models.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    registration_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.username

class Student(GenericUser):
    university_email = models.EmailField(max_length=254)
    telephone_number = models.CharField(max_length=16, null=True)
    personal_email = models.EmailField(max_length=254, null=True)
    facebook_page = models.URLField(max_length=200, null=True)

    MAJORS_NAMES = (
        ('ING_INF_T', 'Ingegneria informatica triennale'),
        ('ING_INF_M', 'Ingegneria informatica magistrale'),
        ('ING_MEC_T', 'Ingegneria meccanica triennale'),
        ('ING_MEC_M', 'Ingegneria meccanica magistrale'),
        ('ING_GES_T', 'Ingegneria gestionale triennale'),
        ('ING_GES_M', 'Ingegneria gestionale magistrale'),

    )

    major = models.CharField(max_length=10, choices=MAJORS_NAMES)
    year_of_study = models.IntegerField(max_length=1, validators=[MaxValueValidator(5), MinValueValidator(1)], default=1)
    sold_books_number = models.IntegerField(default=0)
    bought_books_number = models.IntegerField(default=0)
    reports_number = models.IntegerField(default=0)

    def __str__(self):
        return self.university_email

class Administrator(GenericUser):
    personal_email = models.EmailField(max_length=254)
    handled_reports_number = models.IntegerField(default=0)
    handled_help_req_number = models.IntegerField(default=0)

    def __str__(self):
        return self.personal_email

class Content(models.Model):

    C_TYPES = (
        ('t','title'),
        ('tr', 'title_review'),
        ('ba', 'book_ad'),
        ('ur', 'user_review')
    )
    content_type = models.CharField(max_length=2, choices=C_TYPES)

class Title(models.Model):
    name = models.CharField(max_length=10)
    cover_image = models.ImageField(upload_to='images/title_covers', height_field=None, width_field=None, max_length=100, null=True)
    description = models.TextField(max_length=500)
    #TODO: Content primary key
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='contenuto')
    description_user_id = models.ForeignKey(GenericUser, on_delete=models.SET_NULL, null=True, related_name='descrizioni')
    creation_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_edit_datetime = models.DateTimeField(auto_now=True, auto_now_add=True)

    CATEGORIES = (
        ('FIS', 'Fisica'),
        ('MAT', 'Matematica'),
        ('INF', 'Informatica'),
        ('MEC', 'Meccanica'),
        ('EN', 'Elettronica'),
        ('ECO', 'Economia'),
        ('AUT', 'Automazione'),
        ('STA', 'Statistica')
    )
    category = models.CharField(max_length=3, choices=CATEGORIES)

    def __str__(self):
        return self.name



