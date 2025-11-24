import datetime as dt

from django.core.exceptions import ValidationError


def validate_birthday(value: dt) -> None:
    """Валидация дня рождения."""
    up_boundary = dt.date.today() - dt.timedelta(days=3*365)
    down_boundary = dt.date.today() - dt.timedelta(days=125*365)
    if value > up_boundary:
        raise ValidationError(
            'Вы слишком малы для всех этих дел.'
        )
    if value < down_boundary:
        raise ValidationError(
            'Не может быть Вам столько лет.'
        )
