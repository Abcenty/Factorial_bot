import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

# Переменная, хранящая ответ бота
ANSWER = 1


def multiplication(current, end):
    for i in range(current, end + 1):
        current *= i
    return current


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот, вычисляющий факториалы чисел.\nВведите число\n\n'
                         'Чтобы получить список доступных '
                         'команд - отправьте команду /help')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'Правила пользования ботом:\n\nВы вводите любое натуральное число, '
                         f'а я считаю его факториал.\nВводить текст, спец символы и файлы '
                         f'запрещено\n\nДоступные команды:\n/help - '
                         f'список команд\n'
                         f'\n\nПосчитать факториал?')


# Этот хэндлер будет срабатывать на отправку пользователем чисел
@dp.message(lambda x: x.text and x.text.isdigit())  # and 1 <= int(x.text) <= 100
async def process_numbers_answer(message: Message):
    if int(message.text) > 1500:
        await message.answer(f'Ваше число слишком большое, введите число меньше 1500')
    else:
        answer = multiplication(1, int(message.text))
    if int(message.text) > 1000:
        await message.answer(f'{str(answer)[0:5]}')
    else:
        await message.answer(f'{answer}')


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def process_other_answers(message: Message):
    await message.answer('Я довольно ограниченный бот, введите натуральное число '
                         'и я посчитаю его факториал')


if __name__ == '__main__':
    dp.run_polling(bot)
