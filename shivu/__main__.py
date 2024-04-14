import importlib
import time
import random
import re
import asyncio
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, filters

from shivu import collection, top_global_groups_collection, group_user_totals_collection, user_collection, user_totals_collection, shivuu
from shivu import application, SUPPORT_CHAT, UPDATE_CHAT, db, LOGGER
from shivu.modules import ALL_MODULES



for module_name in ALL_MODULES:
    imported_module = importlib.import_module("shivu.modules." + module_name)




def error_handler(update: Update, context: CallbackContext):
    """Log the error and handle it gracefully."""
    LOGGER.error("An error occurred: %s", context.error)


def main() -> None:
    """Run bot."""

   
    application.add_error_handler(error_handler)


if __name__ == "__main__":
    shivuu.start()
    LOGGER.info("Bot started")
    main()

