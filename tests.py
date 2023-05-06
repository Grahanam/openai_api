import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chatgpt_api_integration(self):
        response = self.app.post('/', data={'chat': 'hello'})
        self.assertEqual(response.status_code, 302)  # Check that the request is successful
        self.assertIn('response:', response.data.decode())  # Check that the response contains the GPT-3 response

    def test_homepage_and_results_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check that the request is successful
        self.assertIn('Chat with OpenAI', response.data.decode())  # Check that the response contains the correct content
