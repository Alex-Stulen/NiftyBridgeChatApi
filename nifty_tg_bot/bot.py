from aiohttp import ClientSession

from aiogram import types

from conf import settings

bot = settings.BOT
dp = settings.BOT_DISPATCHER


@dp.message_handler(commands=['start', ])
async def cmd_start(message: types.Message):
    msg = 'Hi! What would you like to know about Nifty Bridge ? Ask me any questions :)'
    await message.answer(msg)


@dp.message_handler()
async def process_message(message: types.Message):
    answer_message = await message.answer('Loading...')
    failed_msg = 'Failed to process your request. Try again.'

    try:
        async with ClientSession() as session:
            data = {'message': message.text}
            headers = {'X-API-KEY-TOKEN': settings.CHAT_SERVER_ACCESS_TOKEN}
            async with session.post(settings.CHAT_API_ENDPOINT, json=data, headers=headers) as response:
                if response.status != 200:
                    return await answer_message.edit_text(failed_msg)
                else:
                    response_json = await response.json()
                    response_msg = response_json.get('message', '')

                    if not response_msg:
                        response_msg = failed_msg

                    return await answer_message.edit_text(response_msg)
    except Exception as e:
        await answer_message.edit_text(failed_msg)
