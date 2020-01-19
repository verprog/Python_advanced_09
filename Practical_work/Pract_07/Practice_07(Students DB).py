import sqlite3


sqlstr = """select * from students"""

with sqlite3.connect("STUDENTS.db") as conn:
    cursor = conn.cursor()
    execute = cursor.execute(sqlstr)
    data = execute.fetchall()

print(data)