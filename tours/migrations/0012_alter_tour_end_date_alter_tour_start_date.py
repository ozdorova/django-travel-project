# Generated by Django 5.0.6 on 2024-06-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_alter_tour_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конец тура'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Начало тура'),
        ),
    ]
