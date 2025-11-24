from django.db import models


class Contact(models.Model):
    """Модель контактов"""
    name = models.CharField(
        'Название организации',
        max_length=255
    )
    inn = models.CharField(
        'ИНН организации',
        max_length=12
    )
    ogrn = models.CharField(
        'ОГРН организации',
        max_length=13
    )
    legal_address = models.CharField(
        'Юридический адрес',
        max_length=255
    )
    actual_address = models.CharField(
        'Фактический адрес',
        max_length=255
    )
    email = models.EmailField(
        'Адрес электронной почты'
    )
    phone = models.CharField(
        'Телефон',
        max_length=20
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
