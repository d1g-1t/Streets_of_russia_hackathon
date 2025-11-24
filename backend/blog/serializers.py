import datetime as dt

from rest_framework import exceptions, serializers
from blog.models import BlogPost, POST_CHOICES

from aboutus.models import Region
from utils.fields import Base64ImageField
from users.models import CustomUser
from blog.models import BlogPost, Region


class BlogPostSerializer(serializers.ModelSerializer):
    '''Сериализатор для постов в блоге'''
    image = Base64ImageField(required=True, allow_null=False)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    region = serializers.SlugRelatedField(
        queryset=Region.objects.all(),
        many=True,
        slug_field='name',
    )
    relevance_date = serializers.DateField(
        default=(dt.date.today() + dt.timedelta(days=7))
    )
    type = serializers.ChoiceField(choices=POST_CHOICES)

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
            'image',
            'type',
            'relevance_date',
            'region'
        ]

    def validate_image(self, value):
        length = len(value)
        length_mb = round(length / 1048576, 2)
        if length_mb > 8:
            raise exceptions.ValidationError(
                'Размер файла не должен превышать 8 Мб'
            )
        return value

    # def validate(self, data):
    #     print(self.context.get('request'))
    #     return data

    #TODO валидация type, создание relevance_date
    #TODO валидировать географию
