from django.db import models
from . import fields


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=Tour.Status.PUBLISHED)


class Tariff(models.Model):
    """Тарифы проведения тура"""
    title = models.CharField(max_length=50, verbose_name='Название тарифа')
    slug = models.SlugField(max_length=50)
    conditions = models.TextField(verbose_name='Условия тарифа')
    price = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'id'
        ]

        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Place(models.Model):
    """Место, места, область или регион проведения тура"""
    city = models.CharField(max_length=100, verbose_name='Город', blank=True)
    slug = models.SlugField(max_length=100)
    region = models.CharField(max_length=200, verbose_name='Область/Регион')
    country = models.CharField(max_length=200, verbose_name='Страна')

    def __str__(self):
        return f'{self.city}, {self.region}, {self.country}'

    class Meta:
        ordering = [
            'city', 'region'
        ]

        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Tour(models.Model):
    """Тур"""
    class Status(models.IntegerChoices):
        """Статус тура"""
        DRAFT = (0, 'Не активен')
        PUBLISHED = (1, 'Активен')

    # поля
    title = models.CharField(max_length=250, verbose_name='Название тура')
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    tariff = models.ManyToManyField(
        Tariff, related_name='tour_tariff', blank=True, verbose_name='Тарифы')
    place = models.ForeignKey(
        Place, related_name='tour_place', on_delete=models.PROTECT, verbose_name='Места')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(verbose_name='Начало тура')
    end_date = models.DateTimeField(verbose_name='Конец тура')
    is_active = models.BooleanField(
        default=Status.PUBLISHED, verbose_name='Доступен', choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)))
    photo = models.ImageField(
        upload_to=f'tour/%Y/%m/', blank=True)

    active_tours = PublishedManager()
    objects = models.Manager()

    class Meta:
        ordering = [
            '-created'
        ]

        indexes = [
            models.Index(fields=['-created'])
        ]

        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.title


class TourProgramm(models.Model):
    """Программа проведения тура"""
    title = models.CharField(max_length=250, verbose_name='Название')
    tour = models.ForeignKey(Tour, related_name='tour_programm',
                             on_delete=models.CASCADE, verbose_name='Тур')
    order = fields.Odredfield(blank=True, for_fields=[
                              'tour'], verbose_name='День(Автоматический порядок)')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(
        upload_to=f'tour/%Y/%m/', blank=True)

    class Meta:
        ordering = [
            'order'
        ]

        verbose_name = 'Программа тура'
        verbose_name_plural = 'Программы тура'

    def __str__(self):
        return f'{self.order} День'
