from django.test import TestCase
from django.urls import reverse


class SnacksTest(TestCase):
    def test_snack_status_code(self):
        url = reverse("snack_list")
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_snack_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        actual = "snack_list.html"
        self.assertTemplateUsed(response, actual)
