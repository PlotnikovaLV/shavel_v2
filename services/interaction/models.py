from django.db import models

# Create your models here.
class Interaction(models.Model):
    connection = models.CharField('Название отношений', max_length=20)

    def __str__(self):
        return self.connection

    class Meta:
        verbose_name = 'Взаимодействие'
        verbose_name_plural = 'Взаимодействия'

class Object(models.Model):
    name = models.CharField('Название организации', max_length=21, help_text='max 21 символа')
    image_logo = models.ImageField('Логотип', upload_to='static/images/interaction', help_text='не более 200х200')
    con = models.ForeignKey('Interaction', on_delete=models.PROTECT, verbose_name='Отношения')
    # поле ссылается на класс/таблицу Категории: con_id - будет её имя после миграции

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'