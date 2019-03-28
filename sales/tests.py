from django.test import TestCase
from sales import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your tests here.
class HomeViewTest(TestCase):

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ModelsTest(TestCase):

    def test_student(self):
        s = models.Student.objects.create(username='john', email='lennon@thebeatles.com', password='johnpassword')
        self.assertTrue(isinstance(s, models.Student))
        self.assertEqual(str(s), s.email)

    def test_content(self):
        c = models.Content.objects.create(content_type='t')
        self.assertTrue(isinstance(c, models.Content))
        self.assertEqual(str(c), str(c.pk))

    def test_title(self):
        c = models.Content.objects.create(content_type='t')
        t = models.Title.objects.create(isbn='34647458749', name='Funaioli', description='Ingegneria dei sistemi meccanici', content_id=c)
        self.assertTrue(isinstance(t, models.Title))
        self.assertEqual(str(t), str(t.name))

    def test_bookad(self):
        c = models.Content.objects.create(content_type='t')
        t = models.Title.objects.create(isbn='34647458749', name='Funaioli', description='Ingegneria dei sistemi meccanici', content_id=c)
        c2 = models.Content.objects.create(content_type='ba')
        s = models.Student.objects.create(username='john', email='lennon@thebeatles.com', password='johnpassword')

        ba = models.BookAd.objects.create(title_isbn=t, content_id=c2, seller=s, description='Libro in vendita')
        self.assertTrue(isinstance(ba, models.BookAd))
        self.assertEqual(str(ba), str(ba.title_isbn))

    def test_wishlist(self):
        u = models.Student.objects.create(username='jon', email='lennon@thebeatles.com', password='johnpassword')
        c = models.Content.objects.create(content_type='t')
        t = models.Title.objects.create(isbn='34647458749', name='Funaioli', description='Ingegneria dei sistemi meccanici', content_id=c)
        c2 = models.Content.objects.create(content_type='ba')
        s = models.Student.objects.create(username='john', email='lennon@thebeatles.com', password='johnpassword')
        ba = models.BookAd.objects.create(title_isbn=t, content_id=c2, seller=s, description='Libro in vendita')

        w = models.Wishlist(ad_id=ba, user_id=u)
        self.assertTrue(isinstance(w, models.Wishlist))

    def test_interesting_title(self):
        u = models.Student.objects.create(username='giggino', email='lennon@thebeatles.com', password='johnpassword')
        c = models.Content.objects.create(content_type='t')
        t = models.Title.objects.create(isbn='3464758749', name='Funaioli', description='Ingegneria dei sistemi meccanici', content_id=c)
        it = models.InterestingTitle.objects.create(user_id=u, title_isbn=t)

        self.assertTrue(isinstance(it, models.InterestingTitle))