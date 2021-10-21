# Generated by Django 3.2.7 on 2021-09-24 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_message_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='branch',
            field=models.CharField(choices=[('Дзержинск', 'Дзержинск'), ('Столбцы', 'Столбцы'), ('Иное...', 'Иное...')], default='Дзержинск', max_length=20, verbose_name='отделение'),
        ),
    ]
