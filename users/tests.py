from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class CustomUserTest(TestCase):

    def test_homepage_status(self):
        self.helper_status_tests('home')


    def helper_status_tests(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_homepage_template(self):
        self.template_tests('home', 'home.html')

    
    def template_tests(self, url_name, template_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)


class TestModels(TestCase):

        def setUp(self):
            

            self.new_user = CustomUser(
                email='test@email.com',
                password='testing123456'
            )
            self.new_user.save()

        def test_user_exists(self):
            self.user = CustomUser.objects.get(pk=1)
            self.assertEqual(self.new_user, self.user)
            

        def test_duplicate_email(self):
            with self.assertRaises(Exception) as err:
                new_user2 = CustomUser(
                    email='test@email.com',
                    password='newpassword123'
                )
            
                new_user2.save()

            self.assertEqual(IntegrityError, type(err.exception))
