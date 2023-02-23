from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuView
from restaurant.serializers import MenuSerializer

mocks = [
    {
        'title': 'Berry',
        'price': 20.49,
        'inventory': 5,
    },
    {
        'title': 'Efo Riro',
        'price': 12.99,
        'inventory': 4,
    },
    {
        'title': 'Pasta',
        'price': 14.99,
        'inventory': 4,
    },
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for mock in mocks:
            Menu.objects.create(
                title=mock.title,
                price=mock.price,
                inventory=mock.inventory
            )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)
