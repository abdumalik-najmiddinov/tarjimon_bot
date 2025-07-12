import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from googletrans import Translator

API_TOKEN = "BOT_TOKEN"

lists = ["ahmoq", "telba", "jinni", "tupoy"]

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

translator = Translator()


@dp.message(Command("start"))
async def start_handler(message: Message):
    name = message.from_user.full_name
    await message.answer(
        f"✋ <b>{name}! Asalomu Alaykum!\nMen tarjimon botman, matn kiriting, tarjima qilib beraman.</b>"
        , parse_mode="html")


@dp.message(F.text.func(lambda text: text is not None and any(word in text.lower().split() for word in lists)))
async def handle_insult(message: Message):
    await message.reply("Iltimos, odobli bo'ling!")


@dp.message()
async def translate_handler(message: Message):
    text = message.text
    tarjima = translator.translate(text, src='auto', dest='en')
    await message.answer(tarjima.text)


async def on_start_up(dispatcher: Dispatcher):
    await bot.send_message(chat_id="7034143307",
                           text="Bot ishga tushdi")


async def main():
    dp.startup.register(on_start_up)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
