from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from forum.models import Thread, Reply

class ForumViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.thread = Thread.objects.create(title='Test Thread', description='Test Description')
        self.reply = Reply.objects.create(thread=self.thread, user=self.user, message='Test Reply')

    def test_delete_reply_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_reply', args=[self.thread.id, self.reply.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Reply.objects.filter(id=self.reply.id).exists())

    def test_delete_thread_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_thread', args=[self.thread.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Thread.objects.filter(id=self.thread.id).exists())

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/index.html')
        self.assertIn('form', response.context)
        self.assertIn('threads', response.context)
        self.assertIn('latest_thread', response.context)
        self.assertIn('latest_reply', response.context)
        self.assertIn('most_liked_thread', response.context)

    def test_new_thread_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('new_thread'), {'title': 'New Thread', 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Thread.objects.count(), 2)

    def test_thread_view(self):
        response = self.client.get(reverse('thread', args=[self.thread.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread.html')
        self.assertIn('thread', response.context)
        self.assertIn('form', response.context)
        self.assertIn('replies', response.context)

    def test_update_reply_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('update_reply', args=[self.thread.id, self.reply.id]), {'message': 'Updated Reply'})
        self.assertEqual(response.status_code, 302)
        self.reply.refresh_from_db()
        self.assertEqual(self.reply.message, 'Updated Reply')

    def test_update_thread_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('update_thread', args=[self.thread.id]), {'title': 'Updated Thread', 'description': 'Updated Description'})
        self.assertEqual(response.status_code, 302)
        self.thread.refresh_from_db()
        self.assertEqual(self.thread.title, 'Updated Thread')
