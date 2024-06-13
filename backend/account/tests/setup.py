class UserTestSetUpMixin:
    def setUp(self):
        self.register_url = '/api/v1/users/'
        self.activate_url = '/api/v1/users/activation/'
        self.login_url = '/api/v1/token/login/'
        self.user_details_url = '/api/v1/users/'
        self.resend_verification_url = "/api/v1/users/resend_activation/"
        self.send_reset_password_email_url = "/api/v1/users/reset_password/"
        self.confirm_reset_password_url = "/api/v1/users/reset_password_confirm/"

        self.user_data = {
            'email': 'marusya@example.com',
            'username': 'super_koshka',
            'first_name': 'Маруся',
            'last_name': 'Кошковна',
            'password': 'marusya_super_cat_21',
            'confirm_password': 'marusya_super_cat_21',
        }
        self.login_data = {
            'email': 'marusya@example.com',
            'password': 'marusya_super_cat_21'
        }
