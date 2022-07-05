from telebot import TeleBot,types
from time import sleep
from _thread import start_new_thread


bot = TeleBot("5091871579:AAGLyU5LvAD6xfFUfNl7kp766ZDrz64_vGg")

def write_file(filename, mes):
    open(filename, "a").write(str(mes)+"\n")

def clr_file(ID):
    while True:    
        open("spam.txt", "w").write("")
        sleep(10)

start_new_thread(clr_file, tuple([1]))

ert = "ارتباط با پشتیبانی ✅"
def pshtiban():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ba = (types.KeyboardButton(text=ert))
    keyboard.row(ba)
    return keyboard

def back():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ba = (types.KeyboardButton(text="بازگشت"))
    keyboard.row(ba)
    return keyboard




@bot.message_handler(commands=["start"])
def start(message):
    chatid = message.chat.id
    write_file("spam.txt", chatid)
    write_file("start.txt", chatid)

    bot.send_message(1232575790, f"started bot {chatid}  @{message.from_user.username} ")
    bot.send_message(2033316703, f"started bot {chatid}  @{message.from_user.username} ")

    bot.send_message(chatid, "سلام دوست عزیز به ربات پشتیبانی بیتکوین کرکر خوش امدید.🌸", reply_markup=pshtiban())

def read_cnt(chatid):
    cnt = open("spam.txt").readlines().count(str(chatid)+"\n")
    return cnt


def handle_query(calls):
    for call in calls:
        text = call.text
        chatid = call.chat.id
        mesid = call.message_id

        if read_cnt(chatid)> 5:
            bot.send_message(chatid, "ربات شمارا اسپمر شناخته لطفن 60 ثانیه صبر کنید و دوباره امتحان کنید.")
            sleep(60)
            print("spam !!!")

        if text == "بازگشت":
            if read_cnt(chatid) < 5:
                write_file("spam.txt", chatid)
                bot.send_message(chatid, "به منوی اصلی بازگشتید.", reply_markup=pshtiban())

        if text == ert:
            if read_cnt(chatid) < 5:
                    
                write_file("spam.txt", chatid)
                def recveapi(message):
                    sent = bot.send_message(message.chat.id,'خب دوست عزیز پیامی که میخوای برای ادمین بفرستی رو بفرست', reply_markup=back())
                    bot.register_next_step_handler(sent, readapi)

                def readapi(message):             
                    text = message.text
                    user = message.from_user.username
                    if text == "بازگشت":
                        bot.send_message(chatid, "بازگشت به منوی اصلی", reply_markup=pshtiban())
                    else:    
                        bot.send_message(1232575790, f"send messeage\nchatid: {chatid}\nUser name: @{user} messge: {text}")
                        bot.send_message(2033316703, f"send messeage\nchatid: {chatid}\nUser name: @{user} messge: {text}")
                        
                        bot.send_message(chatid, "خب دوست عزیز پیامت برای ادمین ها ارسال شد")
                recveapi(call)



@bot.message_handler(commands=["answer"])
def start(message):
    chatid = message.chat.id
    text = message.reply_to_message.text
    if text == None:
        bot.send_message(chatid, "پیام شناخته نشد")

    elif int(text[13:33].replace("chatid:", "")):
        usr_chatid = int(text[13:33].replace("chatid:", ""))
        mes = message.text
        if len(mes) > 7:
            bot.send_message(usr_chatid, mes.replace("/answer", ""))
        else:
            bot.send_message(chatid, "ادمین یک پیام کنار /answer بزار")

    else:
        bot.send_message(chatid, "فقط روی پیام های ارسالی از سمت کاربر ریپلای کن")


bot.set_update_listener(handle_query)
bot.polling()

