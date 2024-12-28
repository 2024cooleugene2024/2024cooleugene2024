import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
BOT_API = os.getenv('BOT_API')

if BOT_API is None:
    raise ValueError("Не удалось загрузить токен из переменной окружения. Проверьте файл .env.")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),  # Логирование в файл
        logging.StreamHandler()  # Логирование в консоль
    ]
)

bot = Bot(token=BOT_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я ваш Telegram-бот. Чем могу помочь?")
    logging.info(f"Команда /start выполнена для пользователя {message.from_user.id}")


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(f"Он мне ответил: {message.text}")
    logging.info(f"Получено сообщение от пользователя {message.from_user.id}: {message.text}")


if __name__ == '__main__':
    logging.info("Бот запущен.")
    executor.start_polling(dp, skip_updates=True)
