# Generated by Django 5.0.4 on 2024-05-06 10:30

import django.db.models.deletion
import django.db.models.manager
import tours.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('slug', models.SlugField(max_length=100)),
                ('region', models.CharField(max_length=200, verbose_name='Область/Регион')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['city', 'region'],
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название тарифа')),
                ('slug', models.SlugField()),
                ('conditions', models.TextField(verbose_name='Условия тарифа')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название тура')),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(verbose_name='Начало тура')),
                ('end_date', models.DateTimeField(verbose_name='Конец тура')),
                ('is_active', models.BooleanField(choices=[(False, 'Не активен'), (True, 'Активен')], default=1, verbose_name='Статус')),
                ('photo', models.ImageField(blank=True, upload_to='tour/%Y/%m/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tour_place', to='tours.place', verbose_name='Места')),
                ('tariff', models.ManyToManyField(blank=True, related_name='tour_tariff', to='tours.tariff', verbose_name='Тарифы')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
                'ordering': ['-created'],
            },
            managers=[
                ('active_tours', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Programm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('order', tours.fields.Odredfield(blank=True, verbose_name='День(Автоматический порядок)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='tour/%Y/%m/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programm', to='tours.tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Программа тура',
                'verbose_name_plural': 'Программы тура',
                'ordering': ['order'],
            },
        ),
        migrations.AddIndex(
            model_name='tour',
            index=models.Index(fields=['-created'], name='tours_tour_created_e89256_idx'),
        ),
    ]