from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class GenericUser(AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True)
    #password = forms.CharField(widget=forms.PasswordInput)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    registration_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login_datetime = models.DateTimeField(auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return self.username

class Student(GenericUser):
    university_email = models.EmailField(max_length=254, unique=True)
    telephone_number = models.CharField(max_length=16, null=True, unique=True)
    personal_email = models.EmailField(max_length=254, null=True, unique=True)
    facebook_page = models.URLField(max_length=200, null=True, unique=True)

    MAJORS_NAMES = (
        ('ING_INF_T', 'Ingegneria informatica triennale'),
        ('ING_INF_M', 'Ingegneria informatica magistrale'),
        ('ING_MEC_T', 'Ingegneria meccanica triennale'),
        ('ING_MEC_M', 'Ingegneria meccanica magistrale'),
        ('ING_GES_T', 'Ingegneria gestionale triennale'),
        ('ING_GES_M', 'Ingegneria gestionale magistrale'),

    )

    major = models.CharField(max_length=10, choices=MAJORS_NAMES)
    year_of_study = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=1)
    sold_books_number = models.IntegerField(default=0)
    bought_books_number = models.IntegerField(default=0)
    reports_number = models.IntegerField(default=0)

    def __str__(self):
        return self.university_email

class Moderator(GenericUser):
    personal_email = models.EmailField(max_length=254, unique=True)
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
    isbn = models.CharField(max_length=13, primary_key=True, unique=True)
    name = models.CharField(max_length=10)
    cover_image = models.ImageField(upload_to='images/title_covers', height_field=None, width_field=None, max_length=100, null=True)
    description = models.TextField(max_length=500)
    content_id = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='titoli_content')
    description_user_id = models.ForeignKey(GenericUser, on_delete=models.SET_NULL, null=True, related_name='descrizioni')
    creation_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_edit_datetime = models.DateTimeField(auto_now=True, auto_now_add=False)


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

class BookAd(models.Model):
    title_isbn = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='annunci_titolo')
    seller_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='annunci_studente')
    description = models.TextField(max_length=500)
    content_id = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='annunci_content')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    CLASSES = (
        ('A', 'Classe A'),
        ('B', 'Classe B'),
        ('C', 'Classe C'),
        ('D', 'Classe D')
    )
    quality_class = models.CharField(max_length=1, choices=CLASSES)
    publication_datetime = models.DateTimeField(auto_now_add=True)
    last_edit_datetime = models.DateTimeField(auto_now=True)
    buyer_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='acquisti')
    purchase_confirmation = models.BooleanField()

    #NB: Ritorna titolo, non è univoco
    def __str__(self):
        return self.title_isbn

class Wishlist(models.Model):

    ad_id = models.ForeignKey(BookAd, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='wishlist_books')

    class Meta:
        unique_together = (("ad_id", "user_id"),)

class InterestingTitle(models.Model):

    title_isbn = models.ForeignKey(Title, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='interesting_titles')

    class Meta:
        unique_together = (("title_isbn", "user_id"),)


