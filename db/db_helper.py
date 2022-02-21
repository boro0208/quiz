import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("quiz.db")
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    cur = conn.cursor()
    cur.execute("""create table if not exists USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR(255),
    LEVEL VARCHAR(255),SCORE INT);""")
    conn.commit()


def insert_user(conn, user):
    sql = ''' INSERT INTO USERS(USERNAME,LEVEL)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    # return cur.lastrowid


def select_users(conn):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)