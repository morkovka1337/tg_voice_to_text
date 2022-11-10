from aiogram import types, Dispatcher
from loader import bot


# STARTING COMMAND
async def command_start(message : types.Message):
    await message.delete()  # delete /start command from the chat
    await bot.send_message(message.from_user.id, 'Добро пожаловать!'
    )
    await bot.send_message(message.from_user.id,
                           text='Отправьте мне голосовое сообщение, которое необходимо расшифровать'
    )

# CHECKING MESSAGE TYPE
async def check_content_type(message : types.Message):
    if message.content_type == 'voice':
        await bot.send_message(message.from_user.id,
                               text='Ваше голосовое сообщение принято в обработку\nРезультат придет в ближайшее время'
        )
    else:
        await bot.send_message(message.from_user.id,
                               text='Пожалуйста отправьте голосовое сообщение'
        )


# REGISTER HANDLERS
def register_handlers_client(dp : Dispatcher):
    # command start
    dp.register_message_handler(command_start, commands=['старт', 'start', 'начать'])
    dp.register_message_handler(command_start, lambda msg: msg.text.lower() in ['старт', 'start', 'начать'])
    dp.register_message_handler(check_content_type, content_types=types.ContentType.all())