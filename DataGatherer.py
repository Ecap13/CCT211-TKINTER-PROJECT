import sqlite3

conn = sqlite3.connect('Undergrad Program Grades.db')

c = conn.cursor()


def select_program(s):
    c.execute("""SELECT Average_Mark FROM Personal_Grades""")
    m = c.fetchall()

    c.execute("""SELECT Program_Name, Minimum_Required_Mark FROM POST_Admission_Requirements WHERE Program_Name = ?""",
              (s,))
    records = c.fetchall()
    return records, m
