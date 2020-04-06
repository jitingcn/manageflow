from manageflow.test import BaseTestCase
from django.conf import settings


class LoginTestCase(BaseTestCase):
    def setUp(self):
        super(LoginTestCase, self).setUp()
        # self.checks_url =

    def test_username_login(self):
        form = {"login": "user", "password": "password"}
        self.client.post("/login/", form)
        r = self.client.get("/user/boards/")
        self.assertContains(r, "Welcome")

    def test_email_login(self):
        form = {"login": "user@example.org", "password": "password"}
        self.client.post("/login/", form)
        r = self.client.get("/user/boards/")
        self.assertContains(r, "Welcome")

    def test_wrong_password(self):
        form = {"login": "user", "password": "wrong password"}
        r = self.client.post("/login/", form)
        self.assertContains(r, "The username and/or password you specified are not correct.")
