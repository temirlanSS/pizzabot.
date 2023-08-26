from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.management.base import BaseCommand
from bot_tg.bot.buttons import main_keyboard
from telebot import TeleBot, types
from ...models import CustomUser
import telebot
import openai
from telebot import TeleBot

User = get_user_model()

bot = TeleBot(settings.TELEGRAM_TOKEN, threaded=False)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
print(1)
class Command(BaseCommand):
    help = 'bot'

    def handle(self,):
        bot.remove_webhook()
        bot.set_webhook(url=settings.TELEGRAM_WEBHOOK_URL)
        print(3)

@bot.message_handler(commands=['/start',])
def handle_command1(message):
    print(4)
    user_exists = User.objects.filter(chat_id=message.chat.id).exists()
    if not user_exists:
        print(5)
        username = "some_username"  # Здесь подставьте реальное имя пользователя
        user = User(username=username, chat_id=message.chat.id)
        user.save()
        bot.send_message(message.chat.id, f'Вы зарегистрированы как: {username}', reply_markup=main_keyboard())
    else:
        print(6)
        user = User.objects.get(chat_id=message.chat.id)
        username = user.username.split(':')[0]
        bot.send_message(message.chat.id, f'Вы уже зарегистрированы как {username}.', reply_markup=main_keyboard())
