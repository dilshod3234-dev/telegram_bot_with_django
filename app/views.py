# import os , django
# import telebot.types


# from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
# Create your views here.
import os, django

import telebot
from telebot.types import ReplyKeyboardMarkup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from app.models import Category

bot = telebot.TeleBot('5314436530:AAFn0f-VGeav4k-xgi7yzP8FZwdVJClY3zE')


# class Update(View):
#     def post(self , request , *args , **kwargs):
#         data = request.body.decode('utf-8')
#         update = telebot.types.Update.de_json(data)
#         bot.process_new_updates([update])
#         return JsonResponse({'method': 'POST'})
#
#     def get(self , request , *args , **kwargs):
#         return JsonResponse({'method': 'GET'})


@bot.message_handler(func=lambda msg: True)
def start(message):
    categories = Category.objects.all()
    categories_list = [category.name for category in categories]
    rkm = ReplyKeyboardMarkup(True)
    rkm.add(*categories_list)

    bot.send_message(message.chat.id, 'Kategoriyalardan birini tanlang !', reply_markup=rkm)


bot.infinity_polling()
