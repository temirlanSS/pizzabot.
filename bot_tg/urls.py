from django.urls import path
from .management.commands.bot import webhook

app_name = 'bot'

urlpatterns = [
    path('bot/', webhook, name='webhook'),
]
