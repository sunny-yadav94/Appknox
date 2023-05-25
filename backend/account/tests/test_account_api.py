from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from account.views import register
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class AccountUrlsTests(SimpleTestCase):

    def test_get_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)


# class UserAPIViewTests(APITestCase):
#     users_url = reverse('register')

#     def setUp(self):
#         self.user = User.objects.create_user(
#         first_name='sunil', last_name='yadav', email='sunil20@gmail.com', username='sunil20@gmail.com', password='123456')
#         self.token = Token.objects.create(user=self.user)
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Token' + self.token.key)

#     def test_get_users_authenticated(self):
#         response = self.client.get(self.users_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_users_unauthenticated(self):
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(self.users_url)
#         self.assertEquals(response.status_code, 401)