import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
TOKEN = 'YOUR_BOT_TOKEN'
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("Hello! I'm your bot. Type /help for assistance.")

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
