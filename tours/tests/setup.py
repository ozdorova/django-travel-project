from django.test import TestCase
from ..models import Tour, Tariff, Place
from ..utils.funcs import get_tz_time


class TourSetupTestCase(TestCase):
    """Создание моделей для тестов"""

    def setUp(self):
        # Тарифы
        Tariff.objects.create(
            title='Базовый', conditions='Описание базового тарифа', price=10000,
        )
        Tariff.objects.create(
            title='Комфорт', conditions='Описание улучшенного тарифа', price=20000,
        )
        tariffs = Tariff.objects.all()

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
