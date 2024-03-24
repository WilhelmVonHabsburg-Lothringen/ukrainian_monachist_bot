from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from .rputes import film_router,edit_or_answer
from .keyboard import(build_start_menu)
load_dotenv()

root_router = Router()
root_router.include_router(film_router,)

@root_router.message(CommandStart())
async def command_star_handler(message: Message, state:FSMContext) -> None:
    await state.clear()
    await edit_or_answer(message,f"Вітаю,{hbold(message.from_user.full_name)},!\n Оберіть наступний крок, для перегляду коменд використовайте /help", build_start_menu())


async def main() -> None:
    TOKEN = getenv("BOT_TOKEN")
    bot = Bot(TOKEN, parse_mode =ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(root_router)

    await dp.start_polling(bot)

