from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify

from . import fields


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=Tour.Status.PUBLISHED)


class Tariff(models.Model):
    """Тарифы проведения тура"""

    title = models.CharField(
        max_length=50,
        verbose_name='Название тарифа'
    )
    slug = models.SlugField(max_length=50)
    conditions = models.TextField(verbose_name='Условия тарифа')
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['id']

        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class Place(models.Model):
    """Место, места, область или регион проведения тура"""

    # Поля
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        blank=True
    )
    slug = models.SlugField(max_length=100)
    region = models.CharField(
        max_length=200,
        verbose_name='Область/Регион'
    )
    country = models.CharField(
        max_length=200,
        verbose_name='Страна'
    )

    def __str__(self):
        return f'{self.city}, {self.region}, {self.country}' if self.city \
            else f'{self.region}, {self.country}'

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.city:
                self.slug = slugify(f'{self.city}-{self.region}')
            else:
                self.slug = slugify(f'{self.region}-{self.country}')
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['city', 'region']

        indexes = [
            models.Index(fields=['city']),
            models.Index(fields=['region'])
        ]

        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Tour(models.Model):
    """Тур"""

    class Status(models.IntegerChoices):
        """Статус тура"""

        DRAFT = (0, 'Не активен')
        PUBLISHED = (1, 'Активен')

    # Поля
    title = models.CharField(
        max_length=250,
        verbose_name='Название тура'
    )
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    tariffs = models.ManyToManyField(
        Tariff,
        related_name='tour_tariffs',
        blank=True,
        verbose_name='Тарифы'
    )
    places = models.ManyToManyField(
        Place,
        related_name='tour_places',
        verbose_name='Места проведения тура'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(
        verbose_name='Начало тура',
        blank=True
    )
    end_date = models.DateTimeField(
        verbose_name='Конец тура',
        blank=True
    )
    is_active = models.BigIntegerField(
        default=Status.PUBLISHED,
        verbose_name='Статус',
        choices=Status.choices,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Создатель/Организатор',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='tour/%Y/%m/', blank=True)

    # Менеджеры
    active_tours = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-updated']),
            models.Index(fields=['-start_date']),
        ]

        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Programm(models.Model):
    """Программа проведения тура"""

    # Поля
    title = models.CharField(
        max_length=250,
        verbose_name='Название')
    tour = models.ForeignKey(
        Tour,
        related_name='programm',
        on_delete=models.CASCADE,
        verbose_name='Тур'
    )
    order = fields.Odredfield(
        blank=True,
        for_fields=['tour'],
        verbose_name='День(Автоматический порядок)'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='tour/%Y/%m/',
        blank=True
    )

    class Meta:
        ordering = ['order']

        verbose_name = 'Программа тура'
        verbose_name_plural = 'Программы тура'

    def __str__(self):
        return f'{self.order} День'
