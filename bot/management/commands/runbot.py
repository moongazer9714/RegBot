# from telegram import
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler
from django.core.management import BaseCommand
from bot.views import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater("5403002328:AAGyAENo0IV9AZi8hzS1mBmHJyra-4YTa0w")
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, received_message))
        updater.dispatcher.add_handler(MessageHandler(Filters.document, received_file))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, received_contact))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
        updater.start_polling()
        updater.idle()