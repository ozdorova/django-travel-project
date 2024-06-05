

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Tour
from .setup import TourSetupTestCase


class TestListTourViewSet(APITestCase, TourSetupTestCase):

    def setUp(self):
        super().setUp()
        self.client.login(username='test', password='test')

    def test_list_tours(self):
        # пагинация включена
        url = reverse('tour-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)


class TestDetailTourViewSet(TestListTourViewSet):

    def test_create_tour(self):
        url = reverse('tour-list')
        data = {
            'title': 'Новый тур',
            'slug': 'new-tour',
            'description': 'Описание тестового тура',
            'places': [1],
            'is_active': 1,
            'tariffs': [1, 2],
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Tour.objects.filter(title='Новый тур').exists())

    def test_retrieve_tour(self):
        self.test_create_tour()
        tour = Tour.objects.get(title='Новый тур')
        print(tour)
        url = reverse('tour-detail', args=[tour.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Новый тур')

    def test_update_tour(self):
        self.test_create_tour()
        tour = Tour.objects.get(title='Новый тур')
        url = reverse('tour-detail', args=[tour.id])
        data = {'title': 'Новый обновленный тур', 'slug': 'fresh-new-tour'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tour.objects.get(id=tour.id).title, 'Новый обновленный тур')

    def test_delete_tour(self):
        '''Удаление доступно только админу'''
        self.test_create_tour()
        tour = Tour.objects.get(title='Новый тур')
        url = reverse('tour-detail', args=[tour.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Tour.objects.filter(id=tour.id).exists())
