from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.test import APITestCase

from .models import Letter

User = get_user_model()

ENDPOINT = "http://127.0.0.1:8000/"


class LetterTests(APITestCase):
    def setUp(self):
        # create the test sender
        test_sender = User.objects.create(
            username="test_sender",
            email="sender@test.com"
        )
        test_sender.set_password("testpass123")
        test_sender.save()
        self.test_sender = test_sender

        # create the test recipient
        test_recipient = User.objects.create(
            username="test_recipient",
            email="recipient@test.com"
        )
        test_recipient.set_password("testpass123")
        test_recipient.save()
        self.test_recipient = test_recipient

class LetterCreateTests(LetterTests):
    def test_create_letter_draft(self):
        url = ENDPOINT + "letters/"
        data = {
            "recipient": 2,
            "content": "Test content."
        }

        self.client.force_authenticate(self.test_sender)
        response = self.client.post(url, data, format="json")

        # assert letter was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # assert only one letter was created and it contains valid data
        qs = Letter.objects.all()
        letter = qs.get(id=1)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(letter.content, "Test content.")

    def test_create_letter_sent(self):
        url = ENDPOINT + "letters/"
        data = {
            "recipient": 2,
            "content": "Test content.",
            "status": Letter.SENT_STATUS
        }

        self.client.force_authenticate(self.test_sender)
        response = self.client.post(url, data, format="json")

        # assert letter was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # assert only one letter was created and it contains valid data
        qs = Letter.objects.all()
        letter = qs.get(id=1)
        self.assertEqual(qs.count(), 1)
        self.assertEqual(letter.content, "Test content.")
        self.assertEqual(letter.status, Letter.SENT_STATUS)

    def test_create_letter_validators(self):
        url = ENDPOINT + "letters/"
        data = {
            "recipient": 2,
            "content": "Test content.",
            "status": Letter.READ_STATUS  # status not allowed
        }

        self.client.force_authenticate(self.test_sender)
        response = self.client.post(url, data, format="json")

        print(response.data)

        # assert the error message
        self.assertContains(
            response, 
            "status is not allowed",
            count=1,
            status_code=status.HTTP_400_BAD_REQUEST
        )