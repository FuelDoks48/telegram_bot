import telebot

bot = telebot.TeleBot('1659123156:AAG8TYEx3f2m8vs-wONQRwbH82kI_UFiQWg')


@bot.message_handler(commands=['start', 'help'])  # декоратор с помощью которого бот реагирует на команду /start
def start_massage(message):  # Функция реакции на команду
    bot.send_message(message.chat.id, 'Привет я топливный оракул,чем могу быть полезен?')


@bot.message_handler(content_types=['text'])    # Декоратор на контент текста.
def send_text(message):                         # Функция на сообщение
    if message.text.lower() == 'привет':      # Функция реагирует на разный регист,даже если слово по разному напечатано
        bot.send_message(message.chat.id, 'Добро пожаловать, Господин!')
    elif message.text.lower() == 'Прощай' or 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель!')

# Команда для того что бы бот не отключался сразу,а работал и проверял нет ли новых сообщений на сервере
#     |
#     |
#    \ /
#     |
bot.polling()
