from django.db import models


class AboutUs(models.Model):
    """Модель для информации о нас"""
    mission = models.TextField(
        'Миссия'
    )
    history = models.TextField(
        'История'
    )

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class FederalTeam(models.Model):
    """Модель для федеральной команды"""
    name = models.CharField(
        'Наименование',
        max_length=255
    )
    description = models.TextField(
        'Описание'
    )

    class Meta:
        verbose_name = 'Федеральная команда'
        verbose_name_plural = 'Федеральные команды'


class RegionalTeam(models.Model):
    """Модель для региональной команды"""
    name = models.CharField(
        'Наименование',
        max_length=255
    )
    description = models.TextField(
        'Описание'
    )
    region = models.CharField(
        'Регион',
        max_length=255
    )

    class Meta:
        verbose_name = 'Региональная команда'
        verbose_name_plural = 'Региональные команды'


class PartnerType(models.Model):
    """Модель для типов партнеров"""
    TYPE_CHOICES = [
        ('general', 'Генеральные партнеры'),
        ('strategic', 'Стратегические партнеры'),
        ('organizational', 'Организационные партнеры'),
        ('regional', 'Региональные партнеры'),
    ]

    type = models.CharField(
        'Тип',
        max_length=255,
        choices=TYPE_CHOICES
    )

    class Meta:
        verbose_name = 'Тип партнера'
        verbose_name_plural = 'Типы партнеров'


class Partner(models.Model):
    """Модель для партнеров"""
    name = models.CharField(
        'Наименование',
        max_length=255
    )
    description = models.TextField(
        'Описание'
    )
    type = models.ForeignKey(
        PartnerType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип партнера'
    )

    class Meta:
        verbose_name = 'Партнер проекта'
        verbose_name_plural = 'Партнеры проекта'


class Gallery(models.Model):
    """Модель для галереи"""
    name = models.CharField(
        'Название галереи',
        max_length=255
    )
    description = models.TextField(
        'Описание'
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Media(models.Model):
    """Модель для медиа (видео или фото)"""
    gallery = models.ForeignKey(
        Gallery, 
        on_delete=models.CASCADE,
        verbose_name='Галерея'
    )
    file = models.FileField(
        'Файл медиа',
        upload_to='media/'
    )

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class Region(models.Model):
    """Модель для субъектов России"""
    name = models.CharField(
        'Название региона',
        max_length=255
    )

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name
