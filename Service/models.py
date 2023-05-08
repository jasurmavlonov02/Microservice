from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='титле')
    order = models.IntegerField(default=0, verbose_name='ордер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('order',)
        db_table = 'category'


class Service(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    url = models.URLField(max_length=200, verbose_name='урл')
    icon = models.FileField(upload_to='icons', null=True, verbose_name='икона')
    description = models.CharField(max_length=100, default='Онлайн', verbose_name='описание')
    group = models.ForeignKey('GroupService', on_delete=models.CASCADE, related_name='services', verbose_name='группа')
    my_order = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="ордер"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Сервисы'
        verbose_name = 'Сервис'
        ordering = ('my_order',)
        db_table = 'service'


class GroupService(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='имя')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='groups', verbose_name='категория')
    my_order = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="ордер"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Групповое сервисы"
        verbose_name = "Групповое сервис"
        ordering = ('my_order',)
        db_table = 'group_service'

#jasur