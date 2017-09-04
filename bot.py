#!/usr/bin/env python

import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import eliza
import gmail
import helpers

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

gmail_sender = gmail.Gmail('nechemyahome@gmail.com')

updater = Updater(token="430514110:AAG5aF2dSuHJET_dhV77ek-Qv6_wx3_lW2M")
dispatcher = updater.dispatcher

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Hello. How are you feeling today?")

def connect(bot, update):
    gmail_sender.send_message('nirrin@gmail.com', 'Login to Telegram Home Remote Access', helpers.login_message(helpers.generate_secret()))
    bot.send_message(chat_id=update.message.chat_id, text="Connect")

def login(bot, update):
    print update
    bot.send_message(chat_id=update.message.chat_id, text="Login")

def bye(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="See you again")

def snapshot(bot, update):
     bot.send_photo(chat_id=update.message.chat_id, photo=open('cat.jpeg', 'rb'))

def talk(bot, update):
	reply = eliza.analyze(update.message.text)
	bot.send_message(chat_id=update.message.chat_id, text=reply)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('connect', connect))
dispatcher.add_handler(CommandHandler('login', login))
dispatcher.add_handler(CommandHandler('bye', bye))
dispatcher.add_handler(CommandHandler('snapshot', snapshot))

talk_handler = MessageHandler(Filters.text, talk)
dispatcher.add_handler(talk_handler)

updater.start_polling()