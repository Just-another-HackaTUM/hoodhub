from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Topic, Offer


class CreateOfferTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.topic = Topic.objects.get_or_create(name='Test Topic')[0]
        self.client.login(username='testuser', password='testpassword')
        self.create_url = reverse('create')

    def test_create_offer(self):
        data = {
            'title': 'Test Offer',
            'description': 'This is a test offer description.',
            'price': 99.99,
            'start_date': '2023-01-01T00:00:00Z',
            'end_date': '2023-12-31T23:59:59Z',
            'topic': self.topic.identifier,
            'location': 'Test Location'
        }
        response = self.client.post(self.create_url, data)
        print(response)
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Offer created successfully")


class GetOfferTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.offer = Offer.objects.create(
            title='Test Offer',
            author=self.user,
            description='This is a test offer description.',
            price=99.99,
            start_date='2023-01-01T00:00:00Z',
            end_date='2023-12-31T23:59:59Z',
            topic=Topic.objects.get_or_create(name='Test Topic')[0],
            location='Test Location'
        )

        self.get_url = reverse('get_offer', args=[self.offer.identifier])

    def test_get_offer(self):
        response = self.client.get(self.get_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Offer")
        self.assertContains(response, "This is a test offer description.")
        self.assertContains(response, 99.99)
        self.assertContains(response, "2023-01-01T00:00:00Z")
        self.assertContains(response, "2023-12-31T23:59:59Z")
        self.assertContains(response, "Test Topic")
        self.assertContains(response, "Test Location")

    def test_get_offer_not_found(self):
        response = self.client.get(reverse('get_offer', args=['invalid-identifier']))
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Offer not found")
