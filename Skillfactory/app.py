import telebot
from utils import APIException, Convertor
from config import TOKEN, exchanges
import traceback

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = f"Hello {message.chat.username}!\n To convert currency input: <currency to convert> " \
           f"<currency to convert into> " \
           f"<amount of currency>\n" \
           f"To know available currencies type /values "
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Invalid typing!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Error:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Unknown error:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()

