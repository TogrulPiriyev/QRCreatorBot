import os

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import qrcode

#updater = Updater("Key_Code",use_context=True)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)



def unknown(update: Update, context: CallbackContext):
    link = update.message.reply_text(
        "'%s'" % update.message.text)
    print(len(link['text']))
    if len(link['text'])>=30:
        update.message.reply_text(
            "Your link so longer '%s' and we can't create for that QR" % update.message.text)

    img = qrcode.make(link.text.replace("'",""))
    print(link.text.split("'")[1])
    img.save("Hello.png")
    pic = os.path.expanduser("Hello.png")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(pic, 'rb'))

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Enter the text you want to show to the user whenever they start the bot")





updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
