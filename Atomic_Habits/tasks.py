import datetime

from celery import shared_task
from telegram import Bot

from Atomic_Habits.models import Habits
from config import settings

from telegram import Bot
from django.conf import settings


def get_common_chat_id(bot_token):
    bot = Bot(token=bot_token)
    updates = bot.getUpdates()

    if updates:
        chat_id = updates[-1].message.chat_id
        return chat_id

    return None


@shared_task
def send_reminders():
    # Получаем текущее время
    now = datetime.now()
    # Получаем список привычек, о которых нужно напомнить
    habits_to_remind = Habits.objects.filter(
        periodicity__gt=0,  # Выбираем привычки с положительной периодичностью
        time__hour=now.hour,  # Фильтруем привычки по текущему часу
        time__minute=now.minute  # фильтруем привычки по текущей минуте
    )
    # Создаем экземпляр бота с использованием токена из настроек
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    # Получаем chat_id с использованием токена бота

    TELEGRAM_COMMON_CHAT_ID = get_common_chat_id(settings.TELEGRAM_BOT_TOKEN)
    # Перебираем список привычек, которые нужно напомнить
    for habit in habits_to_remind:
        # Создаем текст сообщения с уведомлением о выполнении привычки
        message = f"Время выполнить привычку: {habit.activity}!"
        # Отправляем сообщение в общий чат в Telegram
        bot.send_message(chat_id=TELEGRAM_COMMON_CHAT_ID, text=message)
