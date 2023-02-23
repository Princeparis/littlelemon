from django.test import TestCase
from restaurant.models import Menu


# TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Berry", price=80, inventory=100)
        self.assertEqual(item, "Berry : 80")
