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
