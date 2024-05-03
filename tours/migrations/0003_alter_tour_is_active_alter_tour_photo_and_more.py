# Generated by Django 5.0.4 on 2024-05-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_tour_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Доступен'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='photo',
            field=models.ImageField(blank=True, upload_to='tour/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='tourprogramm',
            name='photo',
            field=models.ImageField(blank=True, upload_to='tour/%Y/%m/'),
        ),
    ]