import telebot
from telebot import types


TOKEN = '7198904076:AAGq0pDnAQ-mAD12R1VeQy1PiWAjDvT9bjI'
bot = telebot.TeleBot(TOKEN)

# приветсвие, команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот для создания задач. Выбери нужную кнопку ниже:)")
    send_menu(message.chat.id)

# основное меню
def send_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Мои задачи')
    btn2 = types.KeyboardButton('Создать задачу')
    btn3 = types.KeyboardButton('История моих задач')
    btn4 = types.KeyboardButton('Редактирование задач')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id, 'Выберите нужное действие:', reply_markup=markup)

# обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Мои задачи':
        # Здесь должна быть логика обработки просмотра задач
        bot.send_message(message.chat.id, "Ваши текущие задачи...")
    elif message.text.strip() == 'Создать задачу':
        # Логика создания новой задачи
        bot.send_message(message.chat.id, "Создание новой задачи...")
    elif message.text.strip() == 'История задач':
        # Логика просмотра истории задач
        bot.send_message(message.chat.id, "История ваших задач...")
    elif message.text.strip() == 'Редактирование':
        # Логика редактирования задач
        bot.send_message(message.chat.id, "Редактирование задач...")
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю эту команду.")
        send_menu(message.chat.id)

# Запуск бота
bot.polling(none_stop=True)