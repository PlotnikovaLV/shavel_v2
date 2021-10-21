from django.db import models

# Create your models here.
class Categorie(models.Model):
    name = models.CharField('Название категории услуг', max_length=20)
    slug = models.SlugField('URL транслитом', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Portfolio(models.Model):
    title = models.CharField('Название услуги', max_length=21, help_text='max 21 символа')
    slug_title = models.SlugField('URL транслитом', max_length=26)
    small_description = models.CharField('Краткое описание', max_length=32, help_text='max 32 символ')
    large_description = models.TextField('Полное описание')
    small_image = models.ImageField('Маленькая картинка', upload_to='static/images/portfolio', help_text='470х330')
    large_image = models.ImageField('Большая картинка', upload_to='static/images/portfolio', help_text='1200х801')
    cat = models.ForeignKey('Categorie', on_delete=models.CASCADE, verbose_name='Категория услуги')
    # поле ссылается на класс/таблицу Категории: cat_id - будет её имя после миграции

    def get_absolute_url(self):    # имя функции зарезервированнное, генерирует обсолютную ссылку на страницу
        return reverse('work', kwargs={'portfolio_slug': self.slug_title})
        # первым атрибутом идет ссылка, вторым атрибутом кваргс - аргументы сформированные в cловарь
        # portfolio_slag - ссылка на которую нажали, self.slug_title - слаг соответсвующий записи в БД

    def __str__(self):
        return self.title

    class Meta:     # локализации в админ панеле - название раздела в общем списке и сам раздел будут так наз-ся
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
