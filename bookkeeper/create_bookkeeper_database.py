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

db_file = "bookkeeper/bookkeeper.db"
for cls in [Category, Expense, Budget]:
    table_name = cls.__name__.lower()
    fields = get_annotations(cls, eval_str=True)
    fields.pop('pk')
    names = ', '.join(fields.keys())
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        cur.execute(f'CREATE TABLE {table_name}({names})')
    con.close()

cat_repo = SQLiteRepository[Category](db_file=db_file, cls=Category)

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
