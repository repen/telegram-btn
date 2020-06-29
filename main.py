#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from threading import Thread
from Control import Controller

# from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity)

TOKEN = '' # Your token for your bot.
controller = Controller()


class Bot:
    def __init__(self):
        self.update_id = None
        self.bot = telegram.Bot(TOKEN)


    def handler(self):
        pass

    def echo(self):

        for update in self.bot.get_updates(offset=self.update_id, timeout=10):
            self.update_id = update.update_id + 1

            if update.message:
        
                markdown, commands = controller.route( update.message.text )

                update.message.reply_markdown(markdown, 
                    reply_markup=telegram.ReplyKeyboardMarkup( commands ))





    def _main(self):

        try:
            self.update_id = self.bot.get_updates()[0].update_id
        except IndexError:
            self.update_id = None

        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        while True:
            try:
                self.echo( )
            except NetworkError:
                sleep(1)
            except Unauthorized:
                # The user has removed or blocked the bot.
                self.update_id += 1

    def main(self):
        self._main()


if __name__ == '__main__':
    bot = Bot()
    bot.main()