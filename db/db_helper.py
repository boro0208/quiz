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
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR(255),
        LEVEL VARCHAR(255),SCORE INT);""")
        conn.commit()
    except Error as e:
        print(e)


def insert_user(conn, user):
    try:
        sql = """INSERT INTO USERS(USERNAME,LEVEL) VALUES(?,?)"""
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
    except Error as e:
        print(e)


def select_users(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def select_user(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, username, level, score FROM users ORDER BY id DESC LIMIT 1")
        rows = cur.fetchall()
        for row in rows:
            return row
    except Error as e:
        print(e)


def update_user(conn, task):
    sql = ''' UPDATE users
              SET score = ? 
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def select_top10_users(conn, task):
    sql = ''' SELECT username, score
              from users
              WHERE level = ?
              order by score desc
              limit 10'''
    cur = conn.cursor()
    cur.execute(sql, (task,))
    rows = cur.fetchall()
    # for row in rows:
    return rows
