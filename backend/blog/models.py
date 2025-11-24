from django.db import models

from aboutus.models import Region
from users.models import CustomUser


POST_CHOICES = (
    ('post', 'Пост'),
    ('reg news', 'Региональная новость'),
    ('fed news', 'Федеральная новость')
)

class BlogPost(models.Model):
    '''Модель для постов в блоге.'''
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор поста',
        # TODO убрать
        null=True
    )
    title = models.CharField(
        'Заголовок',
        max_length=200
    )
    content = models.TextField(
        'Содержание'
    )
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='blogs/images/',
        null=False
    )
    type = models.CharField(
        'Тип поста',
        choices=POST_CHOICES,
        default='post',
        max_length=16
    )
    # TODO: обязательно при простановке новости
    relevance_date = models.DateField(
        'Крайняя дата актуальности новости'
    )
    # TODO: валидация что связь с регионом только если тип новость
    region = models.ManyToManyField(Region, through='PostRegion')

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'

    def __str__(self):
        return '"{}", {}. От {}'.format(
            self.title,
            self.author,
            self.created_at
        )


class PostRegion(models.Model):
    '''Модель связи поста с регионом.'''
    news = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'пост-регион'
        verbose_name_plural = 'посты-регионы'

    def __str__(self):
        return '{}, {}'.format(self.news, self.region)
