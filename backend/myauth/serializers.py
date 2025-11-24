import logging
import sys

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from users.models import CustomUser

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s - строка %(lineno)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.disabled = False
logger.debug('Логирование из auth.serializers запущено')


class MyAuthSerializer(AuthTokenSerializer):
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    email = serializers.EmailField(
        write_only=True
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        read_only=True
    )

    class Meta:
        fields = ('email', 'password')

    def validate(self, data):
        password = data.get('password')
        email = data.get('email')

        if password and email:
            user = None
            try:
                user = CustomUser.objects.get(email=email)
                logger.debug(f'Получен user: {user.__dict__}')
            except CustomUser.DoesNotExist:
                pass

            if not user:
                raise serializers.ValidationError(
                    'Пользователь не зарегистрирован'
                )

            logger.debug('Пользователь распознан как зарегистрированный')

            if not user.check_password(password):
                raise serializers.ValidationError('Пароль неверный')
            logger.debug('Пароль сходится')

        else:
            raise serializers.ValidationError(
                'Не получен пароль и e-mail'
            )
        logger.debug('Пользователь аутентифицирован')
        data['user'] = user
        logger.debug(f'Итоговые data: {data}')
        return data
