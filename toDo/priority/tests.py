from django.test import TestCase
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from priority.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEquals(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf-8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Priority to-do lists</title>', html)

		self.assertTrue(html.endswith('</html>'))