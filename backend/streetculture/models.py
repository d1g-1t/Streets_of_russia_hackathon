from django.db import models


class StreetCulture(models.Model):
    """Модель для уличной культуры"""
    TYPE_CHOICES = [
        ('SKATEBOARD', 'Скейтбординг'),
        ('PARKOUR', 'Паркур'),
        ('WORKOUT', 'Воркаут'),
        ('FREERUN', 'Фриран'),
        ('HIP-HOP DANCE', 'Хип-хоп танцы'),
        ('TRICKING', 'Трикинг'),
        ('RAP', 'Рэп'),
        ('BREAKING', 'Брейк-данс'),
        ('BMX', 'БМХ'),
        ('SKATEBOARDING', 'Скейтбординг'),
        ('SCOOT', 'Скутер')
    ]

    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='streetculture/',
        verbose_name='Фото'
    )
    video = models.URLField(
        verbose_name='Видео'
    )
    culture_type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='SKATEBOARD',
        verbose_name='Тип культуры'
    )

    class Meta:
        verbose_name = 'Уличная культура'
        verbose_name_plural = 'Уличные культуры'

    def __str__(self):
        return self.name
