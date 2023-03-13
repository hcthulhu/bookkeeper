"""
Создание базы данных bookkeeper.db
"""
import sqlite3
from inspect import get_annotations
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.models.budget import Budget
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.utils import read_tree

DB_FILE = "bookkeeper/bookkeeper.db"
for cls in [Category, Expense, Budget]:
    fields = get_annotations(cls, eval_str=True)
    fields.pop('pk')
    with sqlite3.connect(DB_FILE) as con:
        cur = con.cursor()
        cur.execute(f"CREATE TABLE {cls.__name__.lower()}({', '.join(fields.keys())})")
    con.close()

cat_repo = SQLiteRepository[Category](db_file=DB_FILE, cls=Category)

cats = '''
продукты
мясо
    сырое мясо
    мясные продукты
сладости
книги
одежда
'''.splitlines()

Category.create_from_tree(read_tree(cats), cat_repo)
