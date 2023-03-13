"""
Модуль описывает репозиторий, работающий в базе данных SQLite.
"""
import sqlite3
from inspect import get_annotations
from typing import Any

from bookkeeper.repository.abstract_repository import AbstractRepository, T


class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий в базе данных SQLite.
    """
    def __init__(self, db_file: str, cls: type) -> None:
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')
        self.cls = cls

    def add(self, obj: T) -> int:
        if getattr(obj, 'pk', None) != 0:
            raise ValueError(f'trying to add object {obj} with filled `pk` attribute')
        names = ', '.join(self.fields.keys())
        inserts = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(
                f'INSERT INTO {self.table_name} ({names}) VALUES ({inserts})',
                values
            )
            obj.pk = cur.lastrowid
        con.close()
        return obj.pk

    def get(self, pk: int) -> T | None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            row = cur.execute(
                f'SELECT *, ROWID FROM {self.table_name} WHERE ROWID=={pk}'
            ).fetchone()
        con.close()
        if row is None:
            return None
        obj = self.cls(*row)
        return obj

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            if where is None:
                rows = cur.execute(
                    f'SELECT *, ROWID FROM {self.table_name}'
                ).fetchall()
            else:
                conditions = ' AND '.join([f'{f} == ?' for f in where.keys()])
                rows = cur.execute(
                    f'SELECT *, ROWID FROM {self.table_name} WHERE {conditions}',
                    list(where.values())
                ).fetchall()
        con.close()
        return [self.cls(*row) for row in rows]

    def update(self, obj: T) -> None:
        names = ", ".join([f"{f} = ?" for f in self.fields.keys()])
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(
                f'UPDATE {self.table_name} SET {names} WHERE ROWID == {obj.pk}',
                values
            )
            if cur.rowcount == 0:
                raise ValueError('trying to update object with unknown `pk` attribute')
        con.close()

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute(
                f'DELETE FROM  {self.table_name} WHERE ROWID=={pk}'
            )
            if cur.rowcount == 0:
                raise ValueError('trying to update object with unknown `pk` attribute')
        con.close()
