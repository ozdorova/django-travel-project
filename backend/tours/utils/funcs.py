from django.utils import timezone


def get_tz_time(date: str):
    """форматирование даты из строки в дату с текущей зоны для БД"""
    return timezone.datetime.strptime(
        date, '%Y-%m-%d',).astimezone(timezone.get_current_timezone())
