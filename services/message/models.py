from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Message(models.Model):
    THEME_CHOICES = (('Регистрация на сайте', 'Регистрация на сайте'), ('Заключение договора', 'Заключение договора'),
                     ('Заявка на диагностику', 'Заявка на диагностику'), ('Заявка на ремонт', 'Заявка на ремонт'),
                     ('Отзыв', 'Отзыв'), ('Иное...', 'Иное...'))
    BRANCH_CHOICES = (('Дзержинск', 'Дзержинск'), ('Столбцы', 'Столбцы'), ('Иное...', 'Иное...'))
    theme = models.CharField('тема сообщения', max_length=30, choices=THEME_CHOICES)
    name = models.CharField('имя', max_length=35)
    email = models.EmailField('e-mail')
    phone = PhoneNumberField('телефон')
    message = models.TextField('сообщение')
    branch = models.CharField('отделение', max_length=20, choices=BRANCH_CHOICES)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.name