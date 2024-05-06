from django.test import TestCase

from ..utils.funcs import get_tz_time
from ..models import Tour, Tariff, Place


class TourTest(TestCase):
    """ Тест модели Tour, с дополнительными моделями Tariff, Place"""

    def setUp(self):

        # Тарифы
        Tariff.objects.create(
            title='Базовый', conditions='Описание базового тарифа', price=10000,
        )
        Tariff.objects.create(
            title='Комфорт', conditions='Описание улучшенного тарифа', price=20000,
        )
        tariffs = Tariff.objects.all()
        self.tarrifs = tariffs

        # Города(Места)
        place_moscow = Place.objects.create(
            city='Москва', region='Московская область', country='Россия'
        )
        place_obninsk = Place.objects.create(
            city='Обнинск', region='Калужская область', country='Россия'
        )

        # Туры
        Tour.objects.create(
            title='Столица России', description='Описание тура 1',
            place=place_moscow, start_date=get_tz_time('2024-01-01'), end_date=get_tz_time('2024-02-02'),
        ).tariff.set(tariffs)

        Tour.objects.create(
            title='Первый наукоград', description='Описание тура 2',
            place=place_obninsk, start_date=get_tz_time('2024-03-03'), end_date=get_tz_time('2024-04-04'),
        ).tariff.set(tariffs)

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
        stolica, naukograd = Tour.objects.all()
        self.assertEqual(
            stolica.title, 'Первый наукоград'
        )
        self.assertEqual(
            stolica.tariff.first(), self.tarrifs.get(title='Базовый')
        )
        self.assertEqual(
            stolica.place, Place.objects.get(city='Обнинск')
        )
