class UserProfileTestSetUpMixin:
    def setUp(self):
        # создание пользователя через djoser
        self.user = self.client.post(
            '/auth/users/',
            data={
                'username': 'marusya',
                'password': 'i-am-mishas-cat',
            }
        )
        # получение токена jwt
        response = self.client.post(
            '/auth/jwt/create/',
            data={
                'username': 'marusya',
                'password': 'i-am-mishas-cat',
            }
        )
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token}')
