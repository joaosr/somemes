from django.test import TestCase
from django.test.client import Client
from somemes.core.models import Meme
from datetime import datetime


class TestHomeView(TestCase):

    def test_simple_get_request(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(200, response.status_code)

class TestMemeModel(TestCase):

    def setUp(self):
        self.meme = Meme()
        self.meme.descricao = 'Aff'
        self.meme.imagem = ''
        self.meme.save()

    def test_save_meme(self):
        self.assertTrue(Meme.objects.exists())

    def test_list_meme(self):
        list = self.meme.list_all()
        self.assertTrue(len(list) > 0)

    def test_created_at(self):
        self.assertIsInstance(self.meme.created_at, datetime)