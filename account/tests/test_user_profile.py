from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .setup import UserProfileTestSetUpMixin


class TestListUserProfile(UserProfileTestSetUpMixin, APITestCase):
    profile_list_url = reverse('account-list')

    def test_userprofile_list_authenticated(self):
        '''Получение профилей только авторизованным юзерам'''
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestDetailUserProfile(TestListUserProfile):
    def test_userprofile_detail(self):
        response = self.client.get(reverse('account-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_profile(self):
        '''Заполнение профиля'''
        profile = {
            'description': 'Я крутая кошка и зовут меня Маруся',
            'location': 'Обнинск',
        }
        response = self.client.put(
            reverse('account-detail', kwargs={'pk': 1}), data=profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('description' in response.data)
        self.assertTrue('location' in response.data)
