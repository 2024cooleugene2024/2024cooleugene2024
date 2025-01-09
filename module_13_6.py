import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
BOT_API = os.getenv('BOT_API')

if BOT_API is None:
    raise ValueError("Не удалось загрузить токен из переменной окружения. Проверьте файл .env.")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Определяем состояния
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создаем Reply клавиатуру
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton("Рассчитать")
    button_info = KeyboardButton("Информация")
    keyboard.add(button_calculate, button_info)
    return keyboard

# Создаем Inline клавиатуру
def create_inline_keyboard():
    inline_kb = InlineKeyboardMarkup()
    button_calories = InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories")
    button_formulas = InlineKeyboardButton("Формулы расчёта", callback_data="formulas")
    inline_kb.add(button_calories, button_formulas)
    return inline_kb

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = create_main_keyboard()
    await message.answer(
        "Привет! Выберите действие:\n\n- 'Рассчитать', чтобы начать процесс расчета нормы калорий.\n- 'Информация', чтобы узнать больше.",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = create_inline_keyboard()
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора:\n\n"
        "- Для мужчин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) + 5\n"
        "- Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(лет) - 161\n\n"
        "Эта формула используется для расчёта базового метаболизма."
    )
    await call.message.answer(formula)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()  # Устанавливаем состояние age
    await call.message.answer("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await UserState.growth.set()  # Устанавливаем состояние growth
    await message.answer("Введите свой рост (в см):")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await UserState.weight.set()  # Устанавливаем состояние weight
    await message.answer("Введите свой вес (в кг):")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес

    # Получаем все данные
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    # Формула Миффлина - Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    # Для женщин: calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")

    # Завершаем состояние
    await state.finish()

@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    await message.answer(
        "Этот бот помогает рассчитать вашу дневную норму калорий на основе формулы Миффлина-Сан Жеора. "
        "Для расчета укажите ваш возраст, рост и вес. Удачи!"
    )

if __name__ == '__main__':
    logging.info("Бот запущен.")
    executor.start_polling(dp, skip_updates=True)
