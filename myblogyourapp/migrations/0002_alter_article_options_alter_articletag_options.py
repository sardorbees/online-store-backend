# Generated by Django 5.2.1 on 2025-06-05 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogyourapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Медиа статъя', 'verbose_name_plural': 'Медиа статъя'},
        ),
        migrations.AlterModelOptions(
            name='articletag',
            options={'verbose_name': 'Медиа теги', 'verbose_name_plural': 'Медиа теги'},
        ),
    ]
