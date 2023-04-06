import sqlite3

# Starts connection to the database and creates a cursor
conn = sqlite3.connect('Undergrad Program Grades.db')

c = conn.cursor()


# Method that checks if user input exists in the database
def check_program(s):
    check = False
    c.execute("""SELECT Program_Name FROM POST_Admission_Requirements""")
    m = c.fetchall()
    for row in m:
        if row[0] == s:
            check = True
    return check

# Method that checks if user input exists in the database
def list_program():
    check = False
    c.execute("""SELECT Program_Name FROM POST_Admission_Requirements""")
    m = c.fetchall()
    opt = ()
    for row in m:
        opt = opt + row
    return(opt)

# Method used to select the data for the graphs
def select_program(s):
    c.execute("""SELECT Average_Mark FROM Personal_Grades""")
    m = c.fetchall()

    c.execute("""SELECT Program_Name, Minimum_Required_Mark FROM POST_Admission_Requirements WHERE Program_Name = ?""",
              (s,))
    records = c.fetchall()
    return records, m


# Method used to update the records from user input
def edit_student(t):
    c.execute("""UPDATE Personal_Grades SET Average_Grade = ?, Average_Mark = ?, GPA = ?""", (t[0], t[1], t[2],))
    conn.commit()


def quit_database():
    conn.close()
