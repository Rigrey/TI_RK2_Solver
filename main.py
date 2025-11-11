import asyncio
from telebot.async_telebot import AsyncTeleBot, types
import dotenv
from os import getenv

dotenv.load_dotenv()
bot = AsyncTeleBot(token=getenv("TOKEN"))

user_states = {}

# === ЗАДАНИЕ 1 ===
def euler_task(n):
    # TODO: Реализовать логику таски через Эйлера
    res = 0
    return res

def levenshtein_task(n):
    # TODO: Реализовать логику таски через Левенштейна
    res = 0
    return res

# === ЗАДАНИЕ 2 ===
def euler_task_2(n):
    res = 0
    return res

def levenshtein_task_2(n):
    res = 0
    return res

# === ЗАДАНИЕ 3 ===
def task_3_solution(input_data):
    """
    Решение задания 3
    input_data - входные данные
    возвращает результат
    """
    # TODO: Реализовать логику задания 3
    result = f"Результат задания 3 для данных: {input_data}"
    return result

# === ЗАДАНИЕ 4 ===
def task_4_solution(input_data):
    """
    Решение задания 4
    input_data - входные данные
    возвращает результат
    """
    # TODO: Реализовать логику задания 4
    result = f"Результат задания 4 для данных: {input_data}"
    return result


# Обработчики сообщений
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    user_states[message.chat.id] = {'current_task': None}
    await show_main_menu(message.chat.id)


async def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn1 = types.KeyboardButton('📝 Задание 1')
    btn2 = types.KeyboardButton('📝 Задание 2')
    btn3 = types.KeyboardButton('📝 Задание 3')
    btn4 = types.KeyboardButton('📝 Задание 4')

    markup.add(btn1, btn2, btn3, btn4)

    await bot.send_message(
        chat_id,
        "🤖 Добро пожаловать в бот для автоматического решения задач!\n"
        "Выберите задание:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text.startswith('📝 Задание'))
async def handle_task_selection(message):
    chat_id = message.chat.id
    task_number = message.text.split()[1]  # Получаем номер задания

    if task_number == '1':
        await show_task1_menu(chat_id)
    elif task_number == '2':
        await show_task2_menu(chat_id)
    elif task_number == '3':
        await handle_task3(chat_id)
    elif task_number == '4':
        await handle_task4(chat_id)


async def show_task1_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_euler = types.KeyboardButton('🎯 Эйлер (Задание 1)')
    btn_levenshtein = types.KeyboardButton('🔤 Левенштейн (Задание 1)')
    btn_back = types.KeyboardButton('🔙 Назад')

    markup.add(btn_euler, btn_levenshtein, btn_back)

    user_states[chat_id] = {'current_task': '1'}
    await bot.send_message(chat_id, "Выберите тип задания 1:", reply_markup=markup)


async def show_task2_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_euler = types.KeyboardButton('🎯 Эйлер (Задание 2)')
    btn_levenshtein = types.KeyboardButton('🔤 Левенштейн (Задание 2)')
    btn_back = types.KeyboardButton('🔙 Назад')

    markup.add(btn_euler, btn_levenshtein, btn_back)

    user_states[chat_id] = {'current_task': '2'}
    await bot.send_message(chat_id, "Выберите тип задания 2:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in [
    '🎯 Эйлер (Задание 1)', '🔤 Левенштейн (Задание 1)',
    '🎯 Эйлер (Задание 2)', '🔤 Левенштейн (Задание 2)'
])
def handle_specific_task(message):
    chat_id = message.chat.id
    task_text = message.text

    if 'Эйлер' in task_text and 'Задание 1' in task_text:
        bot.send_message(chat_id, "Введите данные для задачи Эйлера (Задание 1):")
        user_states[chat_id]['waiting_for'] = 'euler_1'

    elif 'Левенштейн' in task_text and 'Задание 1' in task_text:
        bot.send_message(chat_id, "Введите две строки для сравнения (через запятую):")
        user_states[chat_id]['waiting_for'] = 'levenshtein_1'

    elif 'Эйлер' in task_text and 'Задание 2' in task_text:
        bot.send_message(chat_id, "Введите данные для задачи Эйлера (Задание 2):")
        user_states[chat_id]['waiting_for'] = 'euler_2'

    elif 'Левенштейн' in task_text and 'Задание 2' in task_text:
        bot.send_message(chat_id, "Введите две строки для продвинутого сравнения (через запятую):")
        user_states[chat_id]['waiting_for'] = 'levenshtein_2'


@bot.message_handler(func=lambda message: message.text == '🔙 Назад')
async def handle_back(message):
    await show_main_menu(message.chat.id)


async def handle_task3(chat_id):
    user_states[chat_id] = {'current_task': '3', 'waiting_for': 'task_3'}
    await bot.send_message(chat_id, "Введите данные для задания 3:")


async def handle_task4(chat_id):
    user_states[chat_id] = {'current_task': '4', 'waiting_for': 'task_4'}
    await bot.send_message(chat_id, "Введите данные для задания 4:")


@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get('waiting_for'))
async def handle_task_input(message):
    chat_id = message.chat.id
    user_state = user_states[chat_id]
    waiting_for = user_state['waiting_for']
    input_data = message.text

    try:
        if waiting_for == 'euler_1':
            result = euler_task(input_data)
            await bot.send_message(chat_id, f"📊 Результат:\n{result}")

        elif waiting_for == 'levenshtein_1':
            result = levenshtein_task(input_data)
            await bot.send_message(chat_id, f"📊 Результат:\n{result}")

        elif waiting_for == 'euler_2':
            result = euler_task_2(input_data)
            await bot.send_message(chat_id, f"📊 Результат:\n{result}")

        elif waiting_for == 'levenshtein_2':
            result = levenshtein_task_2(input_data)
            await bot.send_message(chat_id, f"📊 Результат:\n{result}")

        elif waiting_for == 'task_3':
            result = task_3_solution(input_data)
            await bot.send_message(chat_id, f"📊 Результат задания 3:\n{result}")

        elif waiting_for == 'task_4':
            result = task_4_solution(input_data)
            await bot.send_message(chat_id, f"📊 Результат задания 4:\n{result}")

        # Сбрасываем состояние ожидания
        user_state['waiting_for'] = None

        # Предлагаем вернуться в меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_back = types.KeyboardButton('🔙 Назад')
        markup.add(btn_back)
        await bot.send_message(chat_id, "Выберите следующее действие:", reply_markup=markup)

    except Exception as e:
        await bot.send_message(chat_id, f"❌ Произошла ошибка: {str(e)}")


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling()