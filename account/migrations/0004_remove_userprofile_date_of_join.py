# Generated by Django 5.0.6 on 2024-06-06 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_join',
        ),
    ]