from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Application, ContextTypes
from typing import Final

# Replace 'YOUR_BOT_TOKEN' with the actual API token you obtained from the BotFather
TOKEN = '6647424882:AAH0lBo8-vbd0-NzWY77Qwy3'
BOT_USERNAME = Final = '@Tiktok_Cut_Bot'

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create the bot
    bot = Bot(token=TOKEN)

    # Set up the updater
    updater = Updater(bot=bot, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler (echo all messages)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
