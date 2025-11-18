import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('SELECT name, image_url FROM menu_items LIMIT 5')
rows = cursor.fetchall()
for row in rows:
    print(f'{row[0]}: {row[1][:60] if row[1] else "NULL"}')
conn.close()
