# Generated by Django 3.2.7 on 2021-09-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='theme',
            field=models.CharField(choices=[('Заключение договора', 'Заключение договора'), ('Заявка на диагностику', 'Заявка на диагностику'), ('Заявка на ремонт', 'Заявка на ремонт'), ('Отзыв', 'Отзыв'), ('Иное...', 'Иное...')], max_length=30, verbose_name='тема сообщения'),
        ),
    ]
