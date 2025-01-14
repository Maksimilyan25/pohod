from django.db import models


class Catalog(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=5000)
    image = models.ImageField(
        'Изображение',
        upload_to='static_dev/img/',
        blank=True,
        null=True
        )
    is_published = models.BooleanField(
        'Опубликовано',
        default=False,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    region = models.CharField('Регион', max_length=30, blank=True)
    duration = models.CharField('Длительность', max_length=50, blank=True)
    distance = models.CharField('Расстояние', max_length=255, blank=True)


    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

    def __str__(self):
        return self.title
