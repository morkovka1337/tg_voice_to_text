from aiogram import types, Dispatcher
from loader import bot


# STARTING COMMAND
async def command_start(message: types.Message):
    # delete /start command from the chat
    await message.delete()
    await bot.send_message(
        message.from_user.id,
        text='Добро пожаловать!'
    )
    await bot.send_message(
        message.from_user.id,
        text='Отправьте мне голосовое сообщение, которое необходимо расшифровать'
    )


# CHECKING MESSAGE TYPE
async def check_content_type(message: types.Message):
    # check the type of content
    if message.content_type == 'voice':
        await bot.send_message(
            message.from_user.id,
            text=f'Ваше голосовое сообщение принято в обработку\n'
                 f'Результат придет в ближайшее время'
        )
    else:
        await bot.send_message(
            message.from_user.id,
            text='Пожалуйста отправьте голосовое сообщение'
        )


# REGISTER HANDLERS
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        command_start,
        commands=['старт', 'start', 'начать']
    )
    dp.register_message_handler(
        command_start,
        lambda msg: msg.text.lower() in ['старт', 'start', 'начать']
    )
    dp.register_message_handler(
        check_content_type,
        content_types=types.ContentType.all()
    )
