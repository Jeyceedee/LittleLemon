from django.test import TestCase
from .models import MenuItem
# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = MenuItem.objects.create(title="Chocolate", price=100, inventory=40)
        self.item2 = MenuItem.objects.create(title="Watermelon", price=60, inventory=35)

    def test_getall(self):
        self.assertEqual(str(self.item1), "Chocolate : 100")
        self.assertEqual(str(self.item2), "Watermelon : 60")
