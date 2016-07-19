#!/usr/bin/env python3

import configparser
from telegram.ext import Updater, CommandHandler
import logging
import parrotbot

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    # Read the API key
    config = configparser.ConfigParser()
    config.read('api_key.ini')
    api_key = config.get('api_key', 'api_key')

    updater = Updater(token=api_key)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', parrotbot.start))
    dispatcher.add_handler(CommandHandler('parrot', parrotbot.parrot, pass_args=True))

    updater.start_polling()

if __name__ == '__main__':
    main()