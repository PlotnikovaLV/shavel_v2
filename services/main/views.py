from django.shortcuts import render, redirect, get_object_or_404
from message.forms import MessageForm
from portfolio.models import Portfolio
from portfolio.models import Categorie
from team.models import Team
from interaction.models import Interaction, Object
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm
# from django.urls import reverse_lazy
# from django.contrib.auth.models import *

# Create your views here.
def index(request):
    portfolio_cat = Categorie.objects.all()
    portfolio = Portfolio.objects.all()
    interaction_con = Interaction.objects.all()
    object_int = Object.objects.all()
    data = {
        'portfolio_cat': portfolio_cat,
        'portfolio': portfolio,
        'counter1': 67,
        'counter2': 130,
        'counter3': 27159,
        'interaction_con': interaction_con,
        'object_int': object_int,
        }
    return render(request, 'main/index.html', data)

def work(request, portfolio_slug):
    portfolio_cat = Categorie.objects.all()
    tender = get_object_or_404(Portfolio, slug_title=portfolio_slug)
    data = {
        'portfolio_cat': portfolio_cat,
        'tender': tender,
        }
    return render(request, 'main/work.html', data)

def about(request):
    team = Team.objects.all()
    interaction_con = Interaction.objects.all()
    object_int = Object.objects.all()
    data = {'team': team,
            'interaction_con': interaction_con,
            'object_int': object_int,
            }
    return render(request, 'main/about.html', data)

def contact(request):
    # вывод ошибки, если поле заполненно некорректно
    error_form = ''  # изначально текст ошибки пустой
    # обработка post-запроса; # request.POST формируется как словарь
    if request.method == 'POST':  # если пост запрос был
        message_form = MessageForm(request.POST)  # создается экземпляр класса с данными, переданными пользователем
        if message_form.is_valid():  # если форма заполнена правильно
            message_form.save()  # сохраняем
            return redirect('contact')
        else:
            error_form = 'Некорректные данные! Неверно указан адрес электроннной почты или номер телефона.'  # передаем в словарь data для возможности вывода на сайт

    message_form = MessageForm()
    data = {
        'email': 'beltiar_t@tut.by l.plotnikova.v@gmail.com',
        'address': 'Минская область, г.Дзержинск, ул.Советская, д.5',
        'day_working': 'Работаем пн-пт',
        'working_time1': '08.00 - 13.00',
        'working_time2': '14.00 - 17.00',
        'phone': '+375-33-300-00-20 +375-29-627-26-83',
        'phone2': '8-01718-ХХ-Х-ХХ',
        'message_form': message_form,
        'error_form': error_form}
    return render(request, 'main/contact.html', data)

def branch(request):
# снята форма отсылки сообщений по филиалам и полностью перенесена в Контакты
    # error_form = ''  # изначально текст ошибки пустой
    # # обработка post-запроса; # request.POST формируется как словарь
    # if request.method == 'POST':  # если пост запрос был
    #     message_form = MessageForm(request.POST)  # создается экземпляр класса с данными, переданными пользователем
    #     if message_form.is_valid():  # если форма заполнена правильно
    #         message_form.save()  # сохраняем
    #         return redirect('branch.html')
    #     else:
    #         error_form = 'Некорректные данные! Неверно указан адрес электроннной почты или номер телефона.'
    #
    # message_form = MessageForm()
    data = {
        'email': 'stolbcy_mail@tut.by l.plotnikova.v@gmail.com',
        'address': 'Минская область, г.Столбцы, ул.Социалистическая, д.28',
        'day_working': 'Работаем пн-пт',
        'working_time1': '08.00 - 13.00',
        'working_time2': '14.00 - 17.00',
        'phone': '+375-29-769-45-96',
        'phone2': '8-01717-70-9-26',
        # 'message_form': message_form,
        # 'error_form': error_form,
        }
    return render(request, 'main/branch.html', data)


class LoginUser(LoginView):
    template_name = 'main/login.html'    # имя шаблона( html страницы) для входа

    # def profile(request):
    #     error_form = 'ошибки нету'
    #     if request.user.is_authenticated:
    #         return render(request, 'main/order.html')
    #     else:
    #         error_form = 'Некорректные данные! Неверно указан адрес электроннной почты или номер телефона.'
    #     data = {'error_form': error_form}
    #     return render(request, 'main/login.html', data)

def order(request):
    if request.user.is_authenticated:
        return render(request, 'main/order.html')
    else:
        return render(request, 'main/login.html')
