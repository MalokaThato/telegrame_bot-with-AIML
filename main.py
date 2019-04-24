import telebot
import time

import aiml

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

bot_token = "Key"

bot = telebot.TeleBot(token=bot_token)

def response_func(msg):
    global kernel
    response = kernel.respond(msg)

    if response =="":
        response = "Don't know how to answer that one for now"

    return response

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler(command=['help'])
def send_welcome(message):
    bot.reply_to(message, 'To use this bot, send it a username')


@bot.message_handler(func=lambda msg: msg.text is not None)
def at_answer(message):
    #texts = message.text.split()

    #at_text = find_at(texts)
    print(message)
    response = response_func(message.text)

    bot.reply_to(message, response)



bot.polling()

while True:
    try:
        bot.polling()

    except Exception:
        time.sleep(15)
