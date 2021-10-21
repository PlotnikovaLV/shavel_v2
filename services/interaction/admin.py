from django.contrib import admin
from .models import *
# Register your models here.

class InteractionAdmin(admin.ModelAdmin):
    list_display = ('connection', )

# класс преобразования модели Gallery в панели
class ObjectAdmin(admin.ModelAdmin):   # имена у переменных приведенных в этом классе обязательны
    list_display = ('name', 'con')     # кортеж с именами полей для названия записей в списке
    search_fields = ('name', )  # поля для поиска, в данном случае по названию (см. models.py), кортеж с одним значением, поэтому зпт и пробел
    # list_display_links = () поля в виде ссылок по которым можно переходить в БД

# регистрация моделей
admin.site.register(Interaction, InteractionAdmin)
admin.site.register(Object, ObjectAdmin)