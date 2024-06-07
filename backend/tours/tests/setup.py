from django.contrib.auth.models import User

from ..models import Place, Tariff, Tour
from ..utils.funcs import get_tz_time


class TourTestSetUpMixin:
    '''Создание моделей для тестов'''

    def setUp(self):
        User.objects.create_user(
            username='test',
            password='test'
        )
        # Тарифы
        Tariff.objects.create(
            title='Базовый',
            conditions='Описание базового тарифа',
            price=10000,
        )
        Tariff.objects.create(
            title='Комфорт',
            conditions='Описание улучшенного тарифа',
            price=20000,
        )
        tariffs = Tariff.objects.all()

        # Города(Места)
        place_moscow = Place.objects.create(
            city='Москва',
            region='Московская область',
            country='Россия'
        )
        place_obninsk = Place.objects.create(
            city='Обнинск',
            region='Калужская область',
            country='Россия'
        )

        # Туры
        tour_1 = Tour.objects.create(
            title='Столица России',
            description='Описание тура 1',
            start_date=get_tz_time('2024-01-01'),
            end_date=get_tz_time('2024-02-02'),
            owner=User.objects.get(username='test'),
        )
        tour_1.tariffs.set(tariffs)
        tour_1.places.set([place_moscow])

        tour_2 = Tour.objects.create(
            title='Первый наукоград',
            description='Описание тура 2',
            start_date=get_tz_time('2024-03-03'),
            end_date=get_tz_time('2024-04-04'),
            owner=User.objects.get(username='test'),
        )
        tour_2.tariffs.set(tariffs)
        tour_2.places.set([place_obninsk])

        self._naukograd, self._stolica = Tour.objects.all()
        self._user = User.objects.get(username='test')
