import pytest
import sqlite3
import db

# Фікстура для створення підключення до бази даних
@pytest.fixture
def database():
    conn = sqlite3.connect(':memory:')
    yield conn
    conn.close()

def test_create_schema(database):
    db.create_schema(database)
    cur = database.cursor()
    cur.execute('SELECT * FROM logs')  # Перевірка, чи таблиця існує
    db.create_schema(database)  # Перевірка, чи не буде помилки при створенні таблиці вдруге
