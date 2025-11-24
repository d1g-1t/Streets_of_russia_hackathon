import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('image', models.ImageField(upload_to='blogs/images/', verbose_name='Картинка')),
                ('type', models.CharField(choices=[('post', 'Пост'), ('reg news', 'Региональная новость'), ('fed news', 'Федеральная новость')], default='post', max_length=16, verbose_name='Тип поста')),
                ('relevance_date', models.DateField(verbose_name='Крайняя дата актуальности новости')),
            ],
            options={
                'verbose_name': 'Пост блога',
                'verbose_name_plural': 'Посты блога',
            },
        ),
        migrations.CreateModel(
            name='PostRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutus.region')),
            ],
            options={
                'verbose_name': 'пост-регион',
                'verbose_name_plural': 'посты-регионы',
            },
        ),
    ]
