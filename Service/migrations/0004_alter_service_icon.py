# Generated by Django 4.2 on 2023-05-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0003_alter_service_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.FileField(null=True, upload_to='icons/', verbose_name='икона'),
        ),
    ]