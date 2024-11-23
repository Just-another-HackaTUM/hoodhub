from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Topic, Offer


class CreateOfferTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.topic = Topic.objects.get_or_create(name="Test Topic")[0]
        self.client.login(username="testuser", password="testpassword")
        self.create_url = reverse("create")

    def test_create_offer(self):
        data = {
            "title": "Test Offer",
            "description": "This is a test offer description.",
            "price": 99.99,
            "start_date": "2023-01-01T00:00:00Z",
            "end_date": "2023-12-31T23:59:59Z",
            "topic": self.topic.identifier,
            "location": "Test Location",
        }
        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Offer created successfully")

    def test_create_offer_invalid_topic(self):
        data = {
            "title": "Test Offer",
            "description": "This is a test offer description.",
            "price": 99.99,
            "start_date": "2023-01-01T00:00:00Z",
            "end_date": "2023-12-31T23:59:59Z",
            "topic": "invalid-topic",  # Invalid topic
            "location": "Test Location",
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 400)

    def test_create_offer_invalid_dates(self):
        data = {
            "title": "Test Offer",
            "description": "This is a test offer description.",
            "price": 99.99,
            "start_date": "2023-12-31T23:59:59Z",  # End date before start date
            "end_date": "2023-01-01T00:00:00Z",
            "topic": self.topic.identifier,
            "location": "Test Location",
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 400)


class UpdateOfferTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.offer = Offer.objects.create(
            title="Test Offer",
            author=self.user,
            description="This is a test offer description.",
            price=99.99,
            start_date="2023-01-01T00:00:00Z",
            end_date="2023-12-31T23:59:59Z",
            topic=Topic.objects.get_or_create(name="Test Topic")[0],
            location="Test Location",
        )

        self.client.login(username="testuser", password="testpassword")
        self.update_url = reverse("update")

    def test_update_offer(self):
        data = {
            "identifier": self.offer.identifier,
            "title": "Updated Test Offer",
            "description": "This is an updated test offer description.",
            "price": 199.99,
            "start_date": "2024-01-01T00:00:00Z",
            "end_date": "2024-12-31T23:59:59Z",
            "topic": self.offer.topic.identifier,
            "location": "Updated Test Location",
        }
        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 200)

    def test_update_offer_unauthorized(self):
        user = User.objects.create_user(username="testuser2", password="testpassword")
        self.client.login(username="testuser2", password="testpassword")
        data = {
            "identifier": self.offer.identifier,
            "title": "Updated Test Offer",
            "description": "This is an updated test offer description.",
            "price": 199.99,
            "start_date": "2024-01-01T00:00:00Z",
            "end_date": "2024-12-31T23:59:59Z",
            "topic": self.offer.topic.identifier,
            "location": "Updated Test Location",
        }

        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_offer_invalid_offer(self):
        data = {
            "identifier": "invalid-identifier",  # Invalid identifier
            "title": "Updated Test Offer",
            "description": "This is an updated test offer description.",
            "price": 199.99,
            "start_date": "2024-01-01T00:00:00Z",
            "end_date": "2024-12-31T23:59:59Z",
            "topic": self.offer.topic.identifier,
            "location": "Updated Test Location",
        }
        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_offer_invalid_topic(self):
        data = {
            "identifier": self.offer.identifier,
            "title": "Updated Test Offer",
            "description": "This is an updated test offer description.",
            "price": 199.99,
            "start_date": "2024-01-01T00:00:00Z",
            "end_date": "2024-12-31T23:59:59Z",
            "topic": "invalid-topic",  # Invalid topic
            "location": "Updated Test Location",
        }
        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_offer_invalid_dates(self):
        data = {
            "identifier": self.offer.identifier,
            "title": "Updated Test Offer",
            "description": "This is an updated test offer description.",
            "price": 199.99,
            "start_date": "2024-12-31T23:59:59Z",  # End date before start date
            "end_date": "2024-01-01T00:00:00Z",
            "topic": self.offer.topic.identifier,
            "location": "Updated Test Location",
        }
        response = self.client.post(self.update_url, data)
        self.assertEqual(response.status_code, 400)
