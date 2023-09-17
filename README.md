# Kurs_works_DRF Docker

Сервис, который получает от пользователя привычки и напоминает пользователю об их выполнении.

Проект сделан из двух приложений - users и Atomic_Habits.

✅ Настроены ограничения на аутентификацию и владельца привычки. В случае, если привычка публичкая, то авторизованные
пользователи могут увидеть привычку.

✅Настроены периодические задачи через celery на отправку сообщений в телеграм.

✅ Сделана интеграция с телеграм, подключается запуском файла tg.py. При подключении активируется бот и пользователь при
наборе /start получает сообщения от бота, если у него не занесены привычки. Если же занесены, то бот уведомляет об их
выполнении.
Прежде чем начать использовать проект нужно:
Установить на ПК пакет docker и docker-compose
Создать файл .env для переменного окружения.

Переменные окружения, храняться в файле .env 
Для его создания необходимо переименовать .env-sampel в .env и заполнить своими данными
Пример:
ALLOWED_HOSTS=*
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASES_HOST=db
TELEGRAM_BOT_TOKEN=

Стек технологий:

Django Rest Framework
Celery
PostgreSQL
Flake8
Unittest
drf-yasg
JWT
Telegram
Docker

Запуск Docker проекта:
     --- docker-compose build
     --- docker-compose up

P.S:
- Командой python manage.py create_superuser можно будет добавить учетная запись 2@admin.ru с паролем spartak67 что бы войти в админку
- если команды будут выполняться с ошибкой необходимо  использовать повышение прав sudo