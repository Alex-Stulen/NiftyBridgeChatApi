import os

from aiogram import Bot, Dispatcher


class Settings(object):
    BOT_TOKEN = os.environ['BOT_TOKEN']

    BOT = Bot(token=BOT_TOKEN)
    BOT_DISPATCHER = Dispatcher(BOT)

    CHAT_SERVER_ACCESS_TOKEN = os.environ['CHAT_SERVER_ACCESS_TOKEN']
    CHAT_SERVER_SCHEMA = os.environ['CHAT_SERVER_SCHEMA']
    CHAT_SERVER_HOST = os.environ['CHAT_SERVER_HOST']
    CHAT_SERVER_PORT = os.environ['CHAT_SERVER_PORT']
    CHAT_SERVER_ORIGIN = f'{CHAT_SERVER_SCHEMA}://{CHAT_SERVER_HOST}:{CHAT_SERVER_PORT}'
    CHAT_API_ENDPOINT = f'{CHAT_SERVER_ORIGIN}/api/messages'


settings = Settings()
