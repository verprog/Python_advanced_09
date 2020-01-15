import sqlite3

with sqlite3.connect("SHOP.DB") as conn:
    cursor = conn.cursor()
    result = cursor.execute("""select * from products""")
    data = result.fetchall()
    conn.closed()
    for i in data:
        print(i)