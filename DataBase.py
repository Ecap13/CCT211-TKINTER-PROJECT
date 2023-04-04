"""
Based on the example repository, this file opens and closes the SQL database separate from the main app
"""

import sqlite3


def connect_database():
    global conn, cur

    conn = sqlite3.connect('Undergrad Program Grades.db')

    cur = conn.cursor


def close_database():
    conn.commit()
    conn.close()


if __name__ == '__main__':
    connect_database()
    close_database()
