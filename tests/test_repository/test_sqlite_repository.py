from bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest
import sqlite3
from dataclasses import dataclass

db_file = "bookkeeper/test.db"

@pytest.fixture
def custom_class():
    @dataclass
    class Custom():
        num: int
        name: str = "default"
        pk: int = 0
    return Custom


@pytest.fixture
def create_test_db():
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS custom")
        con.commit()
        cur.execute(f"CREATE TABLE custom(num, name)")
    con.close()


@pytest.fixture
def repo(custom_class, create_test_db):
    return SQLiteRepository(db_file=db_file, cls=custom_class)


def test_crud(repo, custom_class):
    obj1 = custom_class(num=1, name='test 1')
    pk = repo.add(obj1)
    assert obj1.pk == pk
    assert repo.get(pk) == obj1
    obj2 = custom_class(num=2, name='test 2', pk=1)
    repo.update(obj2)
    assert repo.get(pk) == obj2
    repo.delete(pk)
    assert repo.get(pk) is None


def test_cannot_add_with_pk(repo, custom_class):
    obj = custom_class(num=1, name='test 1', pk=1)
    with pytest.raises(ValueError):
        repo.add(obj)


def test_cannot_add_without_pk(repo):
    with pytest.raises(ValueError):
        repo.add(0)


def test_cannot_update_without_pk(repo, custom_class):
    obj = custom_class(num=1, name='test 1', pk=0)
    with pytest.raises(ValueError):
        repo.update(obj)


def test_cannot_update_unexistent(repo, custom_class):
    obj = custom_class(num=1, name='test 1', pk=1)
    with pytest.raises(ValueError):
        repo.update(obj)


def test_get_unexistent(repo):
    assert repo.get(0) is None


def test_get_all(repo, custom_class):
    objects = [custom_class(num=i, name='test') for i in range(5)]
    for o in objects:
        repo.add(o)
    assert objects == repo.get_all()

def test_get_all_with_condition(repo, custom_class):
    objects = [custom_class(num=i, name='test') for i in range(5)]
    for o in objects:
        repo.add(o)
    assert repo.get_all({'num': 0}) == [objects[0]]
    assert repo.get_all({'name': 'test'}) == objects


def test_cannot_delete_unexistent(repo):
    with pytest.raises(ValueError):
        repo.delete(0)
