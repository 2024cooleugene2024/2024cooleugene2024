import logging
import os
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv
from crud_functions import add_user, is_included, get_all_products

# Database setup
DB_PATH = "products.db"  # Database file name

# Load environment variables
load_dotenv()
BOT_API = os.getenv('BOT_API')

if BOT_API is None:
    raise ValueError("Failed to load BOT_API from environment variables. Check your .env file.")

# Logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M')

# Initialize bot and dispatcher
bot = Bot(token=BOT_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Define states
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()  # Default balance of 1000


# Create main keyboard
def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton("Рассчитать")
    button_info = KeyboardButton("Информация")
    button_buy = KeyboardButton("Купить")
    button_register = KeyboardButton("Регистрация")  # New button for registration
    keyboard.add(button_calculate, button_info, button_buy, button_register)
    return keyboard


# Create Inline keyboard
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
        "Привет! Выберите действие:\n\n- 'Рассчитать', чтобы начать процесс расчета нормы калорий.\n"
        "- 'Информация', чтобы узнать больше.\n- 'Купить', чтобы открыть магазин.\n- 'Регистрация', чтобы зарегистрироваться.",
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
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост (в см):")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес (в кг):")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    calories = 10 * weight + 6.25 * growth - 5 * age + 5  # For men
    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал.")
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Информация')
async def send_info(message: types.Message):
    await message.answer(
        "Этот бот помогает рассчитать вашу дневную норму калорий на основе формулы Миффлина-Сан Жеора. "
        "Для расчета укажите ваш возраст, рост и вес. Удачи!"
    )


@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()  # Теперь функция импортирована
    if not products:
        await message.answer("В магазине пока нет доступных товаров.")
        return

    product_kb = InlineKeyboardMarkup()
    for product in products:
        product_id, title, description, price = product
        await message.answer_photo(
            photo=f"https://via.placeholder.com/150?text={title}",  # Placeholder image URL
            caption=f"Название: {title} | Описание: {description} | Цена: {price}"
        )
        product_kb.add(InlineKeyboardButton(title, callback_data=f"product_{product_id}"))

    await message.answer("Выберите продукт для покупки:", reply_markup=product_kb)


@dp.callback_query_handler(lambda call: call.data.startswith('product_'))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split('_')[1]
    await call.message.answer(f"Вы успешно приобрели продукт с ID {product_id}!")


@dp.message_handler(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message):
    await RegistrationState.username.set()
    await message.answer("Введите имя пользователя (только латинский алфавит):")


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
        return

    await state.update_data(username=username)
    await RegistrationState.email.set()
    await message.answer("Введите свой email:")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await RegistrationState.age.set()
    await message.answer("Введите свой возраст:")


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)

    data = await state.get_data()
    username = data.get('username')
    email = data.get('email')
    age = int(data.get('age'))

    # Add user to the database
    add_user(username, email, age)
    await message.answer(f"Регистрация успешна! Добро пожаловать, {username}.")
    await state.finish()


if __name__ == '__main__':
    logging.info("Bot is running.")
    executor.start_polling(dp, skip_updates=True)
