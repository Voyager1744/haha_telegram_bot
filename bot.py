import os

from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from make_joke import get_joke

load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')
CHAT_ID = os.getenv('CHAT_ID')


def wake_up(update, context):
    chat = update.effective_chat
    # name = update.message.chat.title
    button = ReplyKeyboardMarkup(
        [['/start', '/stop'],
         ['Веселый анекдот']],
        resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет! я умею рассказывать анекдоты =)',
        reply_markup=button
    )


def non_stop(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Меня не остановить!')


def say_anything(update, context):
    chat = update.effective_chat
    if update.message.text == 'Веселый анекдот':
        text = get_joke()
        context.bot.send_message(chat_id=chat.id, text=text)


def main():
    updater = Updater(token=TOKEN_BOT)
    updater.dispatcher.add_handler(CommandHandler('stop', non_stop))
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_anything))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
