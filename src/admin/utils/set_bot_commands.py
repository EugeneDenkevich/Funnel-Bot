from aiogram import Bot, types


async def set_bot_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand('homeworks', 'Домашки'),
    ])
