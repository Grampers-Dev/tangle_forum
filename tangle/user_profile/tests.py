from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .views import register, profile, custom_login, custom_logout
from .forms import ExtendedUserCreationForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib import messages

class UserProfileViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user_data = {'username': 'testuser', 'email': 'test@example.com', 'password1': 'testpassword', 'password2': 'testpassword'}

    def test_register_view(self):
        # Create a request object
        request = self.factory.post(self.register_url, self.user_data)

        # Add a session to the request to enable message passing
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = register(request)
        self.assertEqual(response.status_code, 302)  # Check if it redirects
        self.assertTrue(User.objects.filter(username='testuser').exists())  # Check if user is created
        self.assertEqual(messages._queued_messages[0].message, 'Your account has been created. Please log in.')  # Check success message

    def test_profile_view(self):
        # Create a user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Create a request object
        request = self.factory.get(self.profile_url)
        request.user = user

        response = profile(request)
        self.assertEqual(response.status_code, 200)  # Check if it renders the profile template

    def test_login_view(self):
        # Create a user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Create a request object
        request = self.factory.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})

        # Add a session to the request to enable message passing
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = custom_login(request)
        self.assertEqual(response.status_code, 302)  # Check if it redirects

    def test_logout_view(self):
        # Create a user
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Create a request object
        request = self.factory.get(self.logout_url)
        request.user = user

        response = custom_logout(request)
        self.assertEqual(response.status_code, 302)  # Check if it redirects



    ## Add in test case to project, add required files and create the forum app to make this work
