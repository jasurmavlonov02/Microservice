# Generated by Django 4.2 on 2023-05-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='Онлайн', verbose_name='описание'),
        ),
    ]