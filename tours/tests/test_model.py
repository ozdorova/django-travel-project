from ..models import Place, Tariff, Tour
from .setup import TourSetupTestCase


class TourTest(TourSetupTestCase):
    ''' Тест модели Tour, с дополнительными моделями Tariff, Place'''

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
        self.assertEqual(
            self._naukograd.title, 'Первый наукоград'
        )
        self.assertEqual(
            self._stolica.title, 'Столица России'
        )
        self.assertEqual(
            self._naukograd.tariffs.first(), Tariff.objects.get(title='Базовый')
        )
        self.assertQuerysetEqual(
            self._naukograd.places.all(),
            Place.objects.all().filter(city='Обнинск'),
            transform=lambda x: x
        )
        self.assertQuerysetEqual(
            self._stolica.places.all(),
            Place.objects.all().filter(city='Москва'),
            transform=lambda x: x
        )
