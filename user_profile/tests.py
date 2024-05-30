from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from unittest.mock import patch
from user_profile.forms import ExtendedUserCreationForm, ProfileForm
from user_profile.models import Profile

User = get_user_model()

class UserProfileViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    @patch('user_profile.views.send_mail')
    def test_register_view(self, mock_send_mail):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Your account has been created. Please log in.')
        mock_send_mail.assert_called_once()

    def test_register_view_invalid(self):
        invalid_data = self.user_data.copy()
        invalid_data['password2'] = 'differentpassword'
        response = self.client.post(reverse('register'), invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/register.html')
        self.assertFalse(User.objects.filter(username='testuser2').exists())

    def test_profile_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/profile.html')
        self.assertIsInstance(response.context['form'], ProfileForm)

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile'), {
            'bio': 'New bio',
            'location': 'New location',
            'birth_date': '2000-01-01'
        })
        self.assertEqual(response.status_code, 302)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.bio, 'New bio')
        self.assertEqual(profile.location, 'New location')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_view_invalid(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid username or password Please try again')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'You have been logged out.')

    @patch('cloudinary.uploader.upload')
    def test_upload_view_post(self, mock_upload):
        mock_upload.return_value = {'url': 'http://example.com/image.jpg'}
        with open('test_image.jpg', 'wb') as f:
            f.write(b'Test image content')
        with open('test_image.jpg', 'rb') as f:
            response = self.client.post(reverse('upload'), {'image': f})
        self.assertEqual(response.status_code, 200)
        # Add assertions to check if the form saved the image correctly

if __name__ == '__main__':
    TestCase.main()
