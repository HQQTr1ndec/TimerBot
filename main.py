import time
import telebot
from telebot import types
from telebot.types import Message
from CONFIG import TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(["start"])
def start(msg:Message):
    bot.send_message(msg.chat.id,"Привет! Я бот-таймер, если тебе нужно засечить время я тебя помогу")
    qustion(msg)


def qustion(msg:Message):
    kb = types.ReplyKeyboardMarkup(True, True)
    kb.row("минуты")
    kb.row("секунды")
    kb.row("часы")
    bot.send_message(msg.chat.id, "на сколько поставить таймер?", reply_markup=kb)
    bot.register_next_step_handler(msg,check)

def check(msg:Message):
    if msg.text =="минуты":
        bot.send_message(msg.chat.id,"на сколько минут хотите поставить таймер")
        bot.register_next_step_handler(msg,lambda m: set_timer(m,"minutes"))
    elif msg.text == "секунды":
        bot.send_message(msg.chat.id,"на сколько секунд хотите поставить таймер")
        bot.register_next_step_handler(msg,lambda m: set_timer(m,"seconds"))
    elif msg.text =="часы":
        bot.send_message(msg.chat.id, "на сколько часов хотите поставить таймер")
        bot.register_next_step_handler(msg, lambda m: set_timer(m, "hour"))


def set_timer(msg: Message,process:str):
    duration = int(msg.text)
    if not msg.text.isdigit():
        bot.send_message(msg.chat.id,"Нужно ввести число! Попробуй еще раз ")
        return qustion(msg)


    if process =="minutes":
        duration_seconds = duration * 60
        text = f"Таймер на {duration} минут установлен!"
    elif process == "second":
        duration_seconds = duration
        text =f"Таймер на {duration} секунд установлен!"
    elif process =="hour":
        duration_seconds = duration * 3600
        text=f"Таймер на {duration} часов установлен"

    bot.send_message(msg.chat.id,text)
    time.sleep(duration_seconds)
    bot.send_message(msg.chat.id,"ДОБРОЕ УТРО,время пришло")
    bot.send_message(msg.chat.id, "если хочешь посметь запустить меня снова,нажми /start, то будь аккуратен")



# def number_check(msg:Message):
#     if msg.text.isnumeric():
#         time.sleep(int(msg.text))
#         timer_end(msg,int(msg.text))
#     else:
#         bot.send_message(msg.chat.id,"ТЫ отправил не число,попробуй еще раз")
#         qustion(msg)
#
#
# def timer_end(msg:Message,sec:int):
#     bot.send_message(msg.chat.id,"ДОБРОЕ УТРО,время пришло")
#

bot.infinity_polling()


bot.infinity_polling()
