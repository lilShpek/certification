from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
import logging

logger = logging.getLogger('secondapp.views')

# def log(view):
#     def wrapper(request, *args, **kwargs):
#         res = view(request, *args, **kwargs)
#         # print(res.content)
#         logger.info(f'The function {view.__name__} was returned {res.content}')
#         return res
#     return wrapper


# @log
# def gen_coins(request):
#     return HttpResponse(choice(['tail', 'head']))

# @log
# def gen_dice(request):
#     return HttpResponse(choice(['Выпала кость 1', 'Выпала кость 2', 'Выпала кость 3', 'Выпала кость 4', 'Выпала кость 5', 'Выпала кость 6']))

# @log
# def gen_number(request):
#     return HttpResponse(f'Выпало случайное число: {randint(0, 100)}')


def home(request):
    html = '<h1>Добро пожаловать на главную страницу моего сайта!</h1>'
    logger.info("Посещена главная страница")
    return HttpResponse(html)


def about(request):
    html = '<h1>Это страница на которой написано немного информации обо мне</h1><p><h1>Привет! Меня зовут Даниил Калараш, я из города Кишинёв, учусь в школе, в 11 классе, увлекаюсь программированием.</h1></p>'
    logger.info("Посещена страница 'Обо мне'")
    return HttpResponse(html)

# Create your views here.
