from loader import dp
from handlers import user
import json
from aiogram import Bot, Dispatcher, types


async def process_event(event, dp: Dispatcher):
    """
    Converting an Yandex.Cloud functions event to an update and
    handling that update.
    """

    update = json.loads(event['body'])
    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)


async def handler(event, context):
    if event['httpMethod'] == 'POST':
        await user.register_handlers(dp)
        await process_event(event, dp)

        return {'statusCode': 200, 'body': 'ok'}
    return {'statusCode': 405}
