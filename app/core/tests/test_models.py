from django.test import TestCase
from django.contrib.auth import get_user_model


class MotelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull """
        email = 'abm21719@gmail.com'
        password = 'abm123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
