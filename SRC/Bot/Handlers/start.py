from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from SRC.DataBase.Function_Programming_language import get_all_language
from SRC.DataBase.Function_Task import check_answer
from SRC.DataBase.Function_User_DataBase import add_user, issue_task, get_user, true_answer_task, false_answer_task

# Bot setup
bot = Bot("7734808592:AAErqvH9MkIMS8u0h7oK8GwIkEsDh0SMeqg")
dp = Dispatcher(storage=MemoryStorage())

# Keyboards
start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать решать задачи", callback_data="start_tasks")]
    ]
)

language_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python", callback_data="lang_python")],
        [InlineKeyboardButton(text="JavaScript", callback_data="lang_js")],
        [InlineKeyboardButton(text="C#", callback_data="lang_csharp")]
    ]
)

level_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новичок", callback_data="level1")],
        [InlineKeyboardButton(text="Ученик", callback_data="level2")],
        [InlineKeyboardButton(text="Продвинутый", callback_data="level3")],
        [InlineKeyboardButton(text="Разработчик", callback_data="level4")],
        [InlineKeyboardButton(text="Мастер", callback_data="level5")]
    ]
)

answer_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="answer1")],
        [InlineKeyboardButton(text="2", callback_data="answer2")],
        [InlineKeyboardButton(text="3", callback_data="answer3")],
        [InlineKeyboardButton(text="4", callback_data="answer4")]]
)

after_task_true_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить решать задачи", callback_data="after1")],
        [InlineKeyboardButton(text="Поменять язык и сложность", callback_data="after2")]
    ]
)
after_task_false_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продолжить решать задачи", callback_data="after1")],
        [InlineKeyboardButton(text="Повторить попытку", callback_data="after3")],
        [InlineKeyboardButton(text="Поменять язык и сложность", callback_data="after2")],
    ]
)


# FSM states
class Form(StatesGroup):
    waiting_for_language = State()
    waiting_for_level = State()

# Handlers
@dp.message(Command("start"))
async def cmd_start(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username or message.from_user.full_name
    try:
        await add_user(telegram_id, username)
    except:
        pass
    await message.answer(
        "Привет! Я бот 👋\nВот список доступных команд:\n/help — помощь",
        reply_markup=start_kb
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Привет! Я твой помощник, и вот что я могу для тебя сделать:\n"
        "/start — Запуск бота и краткое приветствие.\n"
        "/help — Получить справку и список команд.\n"
        "/achievements — Посмотреть свои достижения."
    )

@dp.callback_query()
async def handle_callbacks(callback: CallbackQuery, state: FSMContext):
    if callback.data == "start_tasks":
        await callback.message.answer(
            "Хорошо! Давай выберем язык программирования и сложность",
            reply_markup=language_kb
        )
        await callback.answer()
        await state.set_state(Form.waiting_for_language)

    elif callback.data == "lang_python":
        await state.update_data(language="Python")
        await callback.message.answer("Вы выбрали Python. Давайте выберем сложность.",
                                      reply_markup=level_kb)
        await callback.answer()

    elif callback.data == "lang_js":
        await state.update_data(language="JavaScript")
        await callback.message.answer("Вы выбрали JavaScript. Давайте выберем сложность.",reply_markup=level_kb)
        await callback.answer()

    elif callback.data == "lang_csharp":
        await state.update_data(language="C#")
        await callback.message.answer("Вы выбрали C#. Давайте выберем сложность.", reply_markup=level_kb)
        await callback.answer()
    elif callback.data == "level1":
        await state.update_data(level="Новичок")
        await callback.message.answer("Вы выбрали 'Новичок', вот задача")
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id,language,level),reply_markup=answer_kb)
        await callback.answer()
    elif callback.data == "level2":
        await state.update_data(level="Ученик")
        await callback.message.answer("Вы выбрали 'Ученик', вот задача")
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id, language, level),reply_markup=answer_kb)
        await callback.answer()
    elif callback.data == "level3":
        await state.update_data(level="Продвинутый")
        await callback.message.answer("Вы выбрали 'Продвинутый', вот задача")
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id, language, level),reply_markup=answer_kb)
        await callback.answer()
    elif callback.data == "level4":
        await state.update_data(level="Разработчик")
        await callback.message.answer("Вы выбрали 'Разработчик', вот задача")
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id, language, level),reply_markup=answer_kb)
        await callback.answer()
    elif callback.data == "level5":
        await state.update_data(level="Мастер")
        await callback.message.answer("Вы выбрали 'Мастер', вот задача")
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id, language, level),reply_markup=answer_kb)
        await callback.answer()
    elif callback.data == "answer1":
        user = await get_user(callback.from_user.id)
        task_id = user.task_id
        if await check_answer(task_id, "1"):
            await true_answer_task(callback.from_user.id)
            await callback.message.answer("Верно",reply_markup=after_task_true_kb)
            await callback.answer()
        else:
            await false_answer_task(callback.from_user.id)
            await callback.message.answer("Неверно",reply_markup=after_task_false_kb)
            await callback.answer()
    elif callback.data == "answer2":
        user = await get_user(callback.from_user.id)
        task_id = user.task_id
        print(task_id)
        if await check_answer(task_id, "2"):
            await true_answer_task(callback.from_user.id)
            await callback.message.answer("Верно",reply_markup=after_task_true_kb)
            await callback.answer()
        else:
            await false_answer_task(callback.from_user.id)
            await callback.message.answer("Неверно",reply_markup=after_task_false_kb)
            await callback.answer()
    elif callback.data == "answer3":
        user = await get_user(callback.from_user.id)
        task_id = user.task_id
        print(task_id)
        if await check_answer(task_id, "3"):
            await true_answer_task(callback.from_user.id)
            await callback.message.answer("Верно",reply_markup=after_task_true_kb)
            await callback.answer()
        else:
            await false_answer_task(callback.from_user.id)
            await callback.message.answer("Неверно",reply_markup=after_task_false_kb)
            await callback.answer()
    elif callback.data == "answer4":
        user = await get_user(callback.from_user.id)
        task_id = user.task_id
        print(task_id)
        if await check_answer(task_id, "4"):
            await true_answer_task(callback.from_user.id)
            await callback.message.answer("Верно", reply_markup=after_task_true_kb)
            await callback.answer()
        else:
            await false_answer_task(callback.from_user.id)
            await callback.message.answer("Неверно",reply_markup=after_task_false_kb)
            await callback.answer()
    elif callback.data == "after1":
        data = await state.get_data()
        language = data.get("language")
        level = data.get("level")
        await callback.message.answer(await issue_task(callback.from_user.id, language, level), reply_markup=answer_kb)
    elif callback.data == "after2":
        await callback.message.answer(
            "Хорошо! Давай выберем язык программирования и сложность",
            reply_markup=language_kb
        )
        await callback.answer()
        await state.set_state(Form.waiting_for_language)
        await callback.answer()
    elif callback.data == "after3":
        await callback.message.answer("Хорошо, пробуй еще раз", reply_markup=answer_kb)
        await callback.answer()


async def on_start():

    await dp.start_polling(bot)