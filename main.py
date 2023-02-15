import logging
import config
import sqlite3
# import filters

from keyboard import greet_kb, markup_fsm_1, markup_fsm_2
# from filters import IsAdminFilter
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup

TOKEN = config.bot_token

# initializing DB
sql = sqlite3.connect("registration.db")
cursor = sql.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
											username TEXT,
											spec TEXT,
											level TEXT
											)""")
print("SQLite table created!")
# prepairing books db

from books_db import b_sql, b_cursor
from books_db import get_sign


# preparing Euler-parser
url = ""


# configure logging
logging.basicConfig(level=logging.INFO)

# initializing storage
storage = MemoryStorage()

# initializing bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


# bind filters
# dp.filters_factory.bind(IsAdminFilter)
#############################################          CLASSES
# books db FSM preparations

class BooksManager(StatesGroup):
	b_name = State()
	b_link = State()
	b_prog = State()
	b_lang = State()


# registration FSM Preparations
class RoleManager(StatesGroup):
	username = State()
	specialization = State()
	prog_level = State()



#############################################             HANDLERS


# GETTING USER REGISTRATION

# starting FSM
@dp.message_handler(commands=['register'])
async def cmd_start(message: types.Message):
	await message.reply("Still good")
	await RoleManager.username.set()

	await message.reply("Enter your username.")

# getting username
@dp.message_handler(state=RoleManager.username)
async def username_get(message: types.Message, state: FSMContext):
	await message.reply("Still good")
	async with state.proxy() as data:
		data['username'] = message.text.lower()

	await RoleManager.next()
	await message.reply("Good. now enter your specialization.", reply_markup=markup_fsm_1)

# getting specialization
@dp.message_handler(state=RoleManager.specialization)
async def get_spec(message: types.Message, state: FSMContext):
	await message.reply("Still good")
	async with state.proxy() as data:
		data['spec'] = message.text.lower()

	await RoleManager.next()
	await message.reply("Perfect. Now, enter your coding level.", reply_markup=markup_fsm_2)

# getting level
@dp.message_handler(state=RoleManager.prog_level)
async def get_level(message: types.Message, state: FSMContext):
	await message.reply("Still good")
	async with state.proxy() as data:
		data['level'] = message.text.lower()

	cursor.execute(f"INSERT INTO users VALUES (?,?,?)", (data['username'], data['spec'], data['level']))
	print("Values got to DB into 'users' table.")
	await message.reply("Successfully registered you!")
	sql.commit()

	await state.finish()
# ENDING USER REGISTRATION

# STARTING GETTING BOOK TO DATABASE


# admin users-check command
@dp.message_handler(commands=['check'])
async def admin_db_check(message: types.Message):
	for value in cursor.execute("SELECT * FROM users"):
		await message.answer(value)


# basic handler
@dp.message_handler(commands=['start', 'hello'])
async def start(message: types.Message):
	await message.reply(config.greeting)
	await message.answer("Good Luck!", reply_markup=greet_kb)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
