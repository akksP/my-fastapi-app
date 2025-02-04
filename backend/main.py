from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

# Замените на свой токен, полученный от BotFather
bot_token = "7319162102:AAEpW1IpILjukNF0fmQOHSXl7HsfR9DmItI"

# URL для Mini App (замените на URL вашего мини-приложения)
mini_app_url = "https://my-fastapi-app-bpr5.onrender.com"  # URL вашего мини-приложения

# Функция обработки команды /start
async def start(update, context):
    # Создаем кнопку, которая откроет Mini App в Telegram
    keyboard = [
        [InlineKeyboardButton("Открыть Mini App", web_app=WebAppInfo(url=mini_app_url))]  # Используем WebAppInfo
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем приветственное сообщение с кнопкой
    await update.message.reply_text(
        text="Добро пожаловать! Нажмите кнопку ниже, чтобы открыть Mini App.",
        reply_markup=reply_markup
    )

# Функция для обработки команды /help
async def help_command(update, context):
    await update.message.reply_text("Напишите /start для начала!")

# Создаем приложение и передаем токен
application = Application.builder().token(bot_token).build()

# Добавляем обработчик для команды /start
application.add_handler(CommandHandler('start', start))

# Добавляем обработчик для команды /help
application.add_handler(CommandHandler('help', help_command))

# Запускаем бота
application.run_polling()