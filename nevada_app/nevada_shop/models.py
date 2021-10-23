from django.db import models


class Group(models.Model):
    photo = models.ImageField(upload_to='photos/', verbose_name='Общее фото')
    description = models.TextField(verbose_name='Общее описание коллектива')

    class Meta:
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллектив'


class Team(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото участника')
    about_me = models.CharField(max_length=1000, verbose_name='О себе')
    comment = models.CharField(max_length=1000, blank=True, verbose_name='Комментарий (не обязательно к заполнению)')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ['pk']


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Repertoire(models.Model):
    name = models.CharField(max_length=256, verbose_name='Композиция')
    comment = models.CharField(max_length=256, blank=True, verbose_name='Комментарий (не обязательно к заполнению)')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Композиция'
        verbose_name_plural = 'Список композиций'
        ordering = ['pk']


class Price(models.Model):
    price = models.CharField(max_length=256, verbose_name='Цена от')
    price_includes = models.TextField(verbose_name='В стоимость входит')
    price_not_include = models.TextField(verbose_name='В стоимость не входит')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото на главной странице')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class CommonRider(models.Model):
    name = models.CharField(max_length=256, verbose_name='Титульник райдера')
    description = models.TextField(verbose_name='Общее описание райдера')

    class Meta:
        verbose_name = 'Райдер общий'
        verbose_name_plural = 'Райдер общий'


class Rider(models.Model):
    name = models.CharField(max_length=256, verbose_name='Райдер')
    file = models.FileField(upload_to='pdf/', verbose_name='PDF-файл')
    short_description = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание')
    main_rider = models.ForeignKey('CommonRider', on_delete=models.CASCADE, verbose_name='Общий райдер')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Райдер'
        verbose_name_plural = 'Райдер'
        ordering = ['pk']
