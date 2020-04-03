from django.test import TestCase
from django.contrib.auth import get_user_model


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        super(BaseTestCase, self).setUp()
        User = get_user_model()
        self.user = User(username="user", email="user@example.org")
        self.user.set_password("password")
        self.user.save()
