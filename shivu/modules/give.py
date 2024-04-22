from telegram import Update
from itertools import groupby
import math
from html import escape 
import random

from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from shivu import collection, user_collection, application


async def give_character_reply(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) != "6257270528":  # Replace "6257270528" with the owner's ID
        await update.message.reply_text('Only the owner can use this command.')
        return

    try:
        # Check if the reply is to a user message
        if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
            await update.message.reply_text('Reply to a user message to give them a character.')
            return

        args = context.args
        if len(args) != 1:
            await update.message.reply_text('Incorrect format. Please use: /give_character_reply character_id')
            return

        character_id = args[0]
        user_id = update.message.reply_to_message.from_user.id

        # Check if the character exists
        character = await collection.find_one({'id': character_id})
        if not character:
            await update.message.reply_text('Character not found.')
            return

        # Update the user's character list with the given character
        await user_collection.update_one(
            {'id': user_id},
            {'$push': {'characters': character}}
        )

        await update.message.reply_text(f'Character "{character["name"]}" has been given to user with ID {user_id}.')
    except Exception as e:
        await update.message.reply_text(f'An error occurred: {str(e)}')


async def give_all_characters(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) != "6257270528":  # Replace "6257270528" with the owner's ID
        await update.message.reply_text('Only the owner can use this command.')
        return

    try:
        # Check if the reply is to a user message
        if not update.message.reply_to_message or not update.message.reply_to_message.from_user:
            await update.message.reply_text('Reply to a user message to give them all characters.')
            return

        user_id = update.message.reply_to_message.from_user.id

        # Get all characters
        all_characters = await collection.find({}).to_list(length=None)

        if not all_characters:
            await update.message.reply_text('No characters found.')
            return

        # Update the user's character list with all characters
        await user_collection.update_one(
            {'id': user_id},
            {'$push': {'characters': {'$each': all_characters}}}
        )

        await update.message.reply_text(f'All characters have been given to user with ID {user_id}.')
    except Exception as e:
        await update.message.reply_text(f'An error occurred: {str(e)}')


GIVE_ALL_CHARACTERS_HANDLER = CommandHandler('giveallc', give_all_characters, block=False)
application.add_handler(GIVE_ALL_CHARACTERS_HANDLER)


GIVE_CHARACTER_REPLY_HANDLER = CommandHandler('givecc', give_character_reply, block=False)
application.add_handler(GIVE_CHARACTER_REPLY_HANDLER)
