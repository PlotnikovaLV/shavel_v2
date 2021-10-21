from django.db import models

# Create your models here.
class Team(models.Model):
    image = models.ImageField('Фото', upload_to='static/images/team', help_text='700х467')
    l_name = models.CharField('Фмилия', max_length=15)
    f_name = models.CharField('Имя', max_length=15)
    patronymic = models.CharField('Отчество', max_length=15)
    post = models.CharField('Должность/род деятельности', max_length=50, help_text='max 50 символ')
    description = models.TextField('Описание', help_text='250 символов')

    def __str__(self):
        return self.l_name

    class Meta:     # локализации в админ панеле - название раздела в общем списке и сам раздел будут так наз-ся
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'