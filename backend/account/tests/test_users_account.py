from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase

from .setup import UserTestSetUpMixin


class TestEmailVerification(UserTestSetUpMixin, APITestCase):
    '''
    Тест верификации по email 
    (Uid + token)
    '''

    def test_register(self):
        '''Простая регистрация без подтверждений'''
        # Регистрация пользователя
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_email_verification(self):
        '''Тест регистрации с верификацией по email'''
        # TODO: Добавить проверку статуса is_active после верификации
        self.test_register()
        self.assertEqual(len(mail.outbox), 1)

        # парсим емейл чтобы достать uid и token
        email_lines = mail.outbox[0].body.splitlines()

        activation_link = [
            link for link in email_lines if "/activate/" in link][0]
        uid, token = activation_link.split("/")[-2:]

        # подтверждение емейла
        data = {"uid": uid, "token": token}
        print(data)
        response = self.client.post(self.activate_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # входим чтобы получить токен
        response = self.client.post(
            self.login_url, self.login_data, format="json")
        self.assertTrue("auth_token" in response.json())
        token = response.json()["auth_token"]

        # забиваем токен в хедерс
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        # просмотр всех пользователей
        # TODO: потом проверить на permission после фронта
        response = self.client.get(self.user_details_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["email"], self.user_data["email"])
        self.assertEqual(response.json()[0]["username"], self.user_data["username"])

    def test_register_resend_verification(self):
        '''Тест на повторную верификацию'''
        self.test_register()

        self.assertEqual(len(mail.outbox), 1)

        response = self.client.post(
            self.login_url, self.login_data, format="json")
        self.assertTrue("auth_token" in response.json())

        token = response.json()["auth_token"]

        # забиваем токен в хедерс
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        # detail пользователя
        response = self.client.get(self.user_details_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # удаляем токен из хедерс
        self.client.credentials()
        # заново высылаем подтверждение
        data = {"email": self.user_data["email"]}
        response = self.client.post(
            self.resend_verification_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # должно быть два емейла в oubox, так как заново выслали верификацию
        self.assertEqual(len(mail.outbox), 2)

        # достаем последний емейл
        email_lines = mail.outbox[1].body.splitlines()
        activation_link = [
            link for link in email_lines if "/activate/" in link][0]
        uid, token = activation_link.split("/")[-2:]

        # подтверждаем емейл
        data = {"uid": uid, "token": token}
        response = self.client.post(self.activate_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_resend_verification_wrong_email(self):
        '''Тест на верификацию с неправильным email'''
        self.test_register()

        # верификация емейла с неправильным емейлом
        data = {"email": self.user_data["email"] + "_this_email_is_wrong"}
        response = self.client.post(
            self.resend_verification_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_activate_with_wrong_uid_token(self):
        '''Тест с неправильным токеном'''
        self.test_register()

        # верификацич с неправильными данными
        data = {"uid": "wrong-uid", "token": "wrong-token"}
        response = self.client.post(self.activate_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
