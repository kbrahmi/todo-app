import sqlite3


def connect():
    return sqlite3.connect('todo-app')


def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            email VARCHAR NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR NOT NULL,
            description VARCHAR,
            status VARCHAR NOT NULL CHECK (status IN ('Not started', 'In progress', 'Completed')),
            assignee_id INTEGER,
            FOREIGN KEY (assignee_id) REFERENCES user(id)
        )
    ''')
    conn.commit()
    conn.close()


def create(table_name, **kwargs):
    conn = connect()
    cursor = conn.cursor()
    columns = ', '.join(kwargs.keys())
    values = ', '.join(['?'] * len(kwargs))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor.execute(query, list(kwargs.values()))
    conn.commit()
    conn.close()


def read_all(table_name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_one(table_name, **kwargs):
    conn = connect()
    cursor = conn.cursor()
    conditions = ' AND '.join([f"{key} = ?" for key in kwargs.keys()])
    query = f'SELECT * FROM {table_name} WHERE {conditions}'
    cursor.execute(query, list(kwargs.values()))
    row = cursor.fetchone()
    conn.close()
    return row


def update(table_name, data, condition):
    conn = connect()
    cursor = conn.cursor()
    set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
    conditions = ' AND '.join([f"{key} = ?" for key in condition.keys()])
    values = list(data.values()) + list(condition.values())
    query = f"UPDATE {table_name} SET {set_clause} WHERE {conditions}"
    cursor.execute(query, values)
    conn.commit()
    conn.close()


def delete(table_name, **kwargs):
    conn = connect()
    cursor = conn.cursor()
    conditions = ' AND '.join([f"{key} = ?" for key in kwargs.keys()])
    query = f'DELETE FROM {table_name} WHERE {conditions}'
    cursor.execute(query, list(kwargs.values()))
    conn.commit()
    conn.close()
