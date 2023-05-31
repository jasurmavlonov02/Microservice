# Generated by Django 4.2 on 2023-05-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
	("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Названия категории')),
                ('order', models.IntegerField(default=0, verbose_name='группировка')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'category',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Названия сервисов')),
                ('url', models.URLField(verbose_name='урл')),
                ('icon', models.FileField(null=True, upload_to='icons', verbose_name='икона')),
                ('description', models.CharField(default='Онлайн', max_length=100, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='GroupService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Названия группы')),
                ('my_order', models.IntegerField(default=0, verbose_name='группировка')),
                ('category', models.ManyToManyField(related_name='groups', to='Service.category', verbose_name='категория')),
                ('service', models.ManyToManyField(to='Service.service')),
            ],
            options={
                'verbose_name': 'Группы',
                'verbose_name_plural': 'Группы',
                'db_table': 'group_service',
                'ordering': ('my_order',),
            },
        ),
    ]
