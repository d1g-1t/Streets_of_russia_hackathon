import logging
import sys

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from streets_backend.settings import EMPTY_VALUE

from .models import CustomUser, UserRegion

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s - строка %(lineno)s'
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)
handler.setFormatter(formatter)
logger.disabled = False
logger.debug('Логирование из admin.users запущено')

# отключение отображения в админ-панели раздела 'пользователи и группы'
admin.site.unregister(Group)


@admin.register(CustomUser)
class UserAdminConfig(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_active'
    )
    search_fields = ('username', 'email')

    list_filter = ('email', 'username', 'is_superuser', 'is_staff')

    fieldsets = (
        ('Ключевая информация', {
            'fields': ('avatar', 'username', 'email', 'password')
        }),
        ('Персональные данные', {
            'fields': (
                'first_name',
                'last_name',
                'third_name',
                'bio',
                'summary_bio',
                'birth_date'
            ),
            'classes': ('collapse',)
        }),
        ('Контактная информация', {
            'fields': (
                'tg_nick', 'phone'
            ), 'classes': ('collapse',)
        }),
        ('Доступ', {
            'fields': ('role', 'is_staff', 'is_active', 'is_superuser')}),
    )

    # readonly_fields = (
    #     'username',
    #     'email',
    #     'first_name',
    #     'last_name',
    #     'is_staff'
    # )

    add_fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': (
                'role',
                'username',
                'email',
                'password1',
                'password2'
            )
        }),
    )
    empty_value_display = EMPTY_VALUE

    def save_model(self, request, obj, form, change):
        """Кастомизированный метод сохранения пользователя из админ панели."""
        logger.debug(change)
        if isinstance(obj, CustomUser):
            logger.debug('The object was recognized as CustomUser instance')
            super().save_model(request, obj, form, change)
            user_role = obj.role
            logger.debug('user\'s role: %s', user_role)
            username = obj.username
            if user_role in (
                'admin',
                'fed manager',
                'reg manager'
            ):
                obj.is_staff = True
            # на случай изменения объекта
            else:
                obj.is_staff = False
            obj.save()
            if change:
                if obj.is_superuser:
                    logger.debug(
                        f'\tВНИМАНИЕ! Объект был изменен на '
                        f'"суперпользователь {username}".')
                else:
                    logger.debug(
                        f'\tВНИМАНИЕ! Объект был изменен на '
                        f'"пользователь {username}".'
                    )
            else:
                if obj.is_superuser:
                    logger.debug(f'Создан суперпользователь {username}.')
                else:
                    logger.debug(f'Создан пользователь {username}.')
            # при запуске в производство поставить отправку по почте
            logger.debug(
                f'Его роль: {user_role}.\n'
            )
            logger.debug(f'user is active: {obj.is_active}')
            logger.debug(f'user is staff: {obj.is_staff}')
        else:
            super().save_model(request, obj, form, change)


@admin.register(UserRegion)
class UserRegionAdminConfig(admin.ModelAdmin):
    list_display = ('region', 'user')
    add_fieldsets = (None, {'fields': ('region', 'user')})
