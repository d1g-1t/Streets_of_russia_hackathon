from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import qrcode
from decouple import Config

config = Config(".env")


class QRCode(models.Model):
    '''Модель QR-кода'''
    event = models.OneToOneField(
        'Event',
        on_delete=models.CASCADE,
        related_name='qrcode'
    )
    image = models.ImageField(
        upload_to='qrcodes',
        blank=True
    )


class Event(models.Model):
    '''Модель мероприятия'''
    EVENT_TYPES = (
        ('competition', 'Соревнование'),
        ('training', 'Тренировка'),
        ('event', 'Мероприятие'),
    )

    DISCIPLINES = (
        ('STREET-ART', 'STREET-ART'),
        ('PARKOUR', 'PARKOUR'),
        ('WORKOUT', 'WORKOUT'),
        ('БМХ', 'БМХ'),
        ('СКЕЙТБОРДИНГ', 'СКЕЙТБОРДИНГ'),
        ('ТРЮКОВОЙ САМОКАТ', 'ТРЮКОВОЙ САМОКАТ'),
        ('ФРИРАН', 'ФРИРАН'),
        ('ТРИКИНГ', 'ТРИКИНГ'),
        ('БРЕЙК-ДАНС', 'БРЕЙК-ДАНС'),
        ('ГРАФФИТИ', 'ГРАФФИТИ'),
        ('ДИДЖЕИНГ', 'ДИДЖЕИНГ'),
        ('РЕП', 'РЕП'),
    )

    name = models.CharField(
        'Название мероприятия',
        max_length=255
    )
    time = models.TimeField(
        'Время проведения'
    )
    date = models.DateField(
        'Дата проведения'
    )
    place = models.CharField(
        'Место проведения',
        max_length=255
    )
    description = models.TextField(
        'Описание мероприятия'
    )
    region = models.CharField(
        'Регион',
        max_length=255
    )
    event_type = models.CharField(
        'Тип события',
        max_length=50,
        choices=EVENT_TYPES
    )
    discipline = models.CharField(
        'Дисциплина',
        max_length=50,
        choices=DISCIPLINES
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_qr_code()

    def create_qr_code(self):
        qrcode_img = qrcode.make(
            config('SERVER_IP') + 
            reverse('event-detail', args=[str(self.id)])
        )
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qrcode-{self.id}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        file = File(buffer, fname)
        if hasattr(self, 'qrcode'):
            self.qrcode.image.save(fname, file, save=True)
        else:
            QRCode.objects.create(event=self, image=file)
        canvas.close()

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name


class QRCodeDownloadView(UserPassesTestMixin, View):
    '''Представление для скачивания QR-кода'''
    def test_func(self):
        return self.request.user.role in ['admin', 'fed manager', 'reg manager']

    def handle_no_permission(self):
        return HttpResponse(status=403)

    def get(self, request, *args, **kwargs):
        event = Event.objects.get(id=kwargs['pk'])
        img = Image.open(event.qrcode.image)
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        return response


class Coordinates(models.Model):
    '''Модель координат'''
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'


class EventLocation(models.Model):
    '''Модель местоположения мероприятия'''
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    coordinates = models.OneToOneField(
        Coordinates,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
