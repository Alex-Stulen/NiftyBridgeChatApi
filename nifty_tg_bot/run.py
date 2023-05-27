from aiogram import Dispatcher, executor

from bot import dp


async def on_startup(dispatcher: Dispatcher):
    print('Bot started and ready to receive messages')


async def on_shutdown(dispatcher: Dispatcher):
    print('Bot has finished')


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )
