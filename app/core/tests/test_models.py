from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
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
    def test_new_user_email_normalize(self):
        """ Test the email of  a new user is normalized"""
        email = 'test@ABM21719.COM'
        user = get_user_model().objects.create_user(email, 'abm123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """ Test creating user without email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abm123')



    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@techchannel.com',
            'abm123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
