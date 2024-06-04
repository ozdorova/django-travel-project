from ..models import Tour, Tariff, Place
from .setup import TourSetupTestCase


class TourTest(TourSetupTestCase):
    """ Тест модели Tour, с дополнительными моделями Tariff, Place"""

    def test_places(self):
        place_moscow = Place.objects.get(city='Москва')
        place_obninsk = Place.objects.get(city='Обнинск')

        self.assertEqual(
            place_moscow.city, 'Москва'
        )
        self.assertEqual(
            place_moscow.slug, 'moskva-moskovskaya-oblast'
        )
        self.assertEqual(
            place_obninsk.city, 'Обнинск'
        )
        self.assertEqual(
            place_obninsk.slug, 'obninsk-kaluzhskaya-oblast'
        )

    def test_tariffs(self):
        base, _ = Tariff.objects.all()
        self.assertEqual(
            base.title, 'Базовый'
        )
        self.assertEqual(
            base.slug, 'bazovyij'
        )

    def test_tours(self):
        # ИСПРАВИТЬ
        stolica, naukograd = Tour.objects.all()
        self.assertEqual(
            naukograd.title, 'Первый наукоград'
        )
        self.assertEqual(
            stolica.title, 'Москва'
        )
        self.assertEqual(
            naukograd.tariff.first(), Tariff.objects.get(title='Базовый')
        )
        self.assertEqual(
            naukograd.place, Place.objects.get(city='Обнинск')
        )
        self.assertEqual(
            stolica.place, Place.objects.get(city='Москва')
        )
