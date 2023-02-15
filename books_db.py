import sqlite3

# prepairing DB instruments

b_sql = sqlite3.connect("books.db")
b_cursor = b_sql.cursor()

# creating DB

b_cursor.execute("""CREATE TABLE IF NOT EXISTS books(
name TEXT,
link TEXT,
prog_lang TEXT,
lang TEXT)""")

test = input("Enter test  name")

def get_sign(db_data):
	b_cursor.execute("INSERT INTO books VALUES (?,?,?,?)", db_data)
	b_sql.commit()

b_name = input("Enter book's name: ")
b_link = input("Enter book's link: ")
b_prog = input("Enter book's prog.language: ")
b_lang = input("Enter book's language: ")

data = [b_name, b_link, b_prog, b_lang]

get_sign(data)
