from django.contrib import admin
from .models import *

# Register your models here.
class MessageAdmin(admin.ModelAdmin):   # имена у переменных приведенных в этом классе обязательны
    list_display = ('name', 'branch')     # кортеж с именами полей для названия записей в списке
    search_fields = ('branch', 'name')  # поля для поиска, в данном случае по названию (см. models.py), кортеж с одним значением, поэтому зпт и пробел
    # list_display_links = () поля в виде ссылок по которым можно переходить в БД

admin.site.register(Message, MessageAdmin)
