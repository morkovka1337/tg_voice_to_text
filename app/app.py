from aiogram.utils import executor
from loader import dp, bot
from handlers import client
from data import config


async def on_startup(_):
    #await bot.set_webhook(config.WEBAPPURL)
    print('Bot has been successfully activated!')

# async def on_shutdown(dp):
#     await bot.delete_webhook()


if __name__ == "__main__":
    client.register_handlers_client(dp)  # register client handlers
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path='',
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=config.WEBAPPHOST,
    #     port=config.WEBAPPPORT
    # )