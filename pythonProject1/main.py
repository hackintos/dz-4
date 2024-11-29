import sqlite3

conn = sqlite3.connect('FruitBasket.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Fruits (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Назва_фрукта TEXT NOT NULL, 
    Колір TEXT NOT NULL 
)
''')


cursor.execute('DELETE FROM Fruits')
conn.commit()


cursor.executemany('''
INSERT INTO Fruits (Назва_фрукта, Колір) 
VALUES (?, ?)
''', [
    ('Яблуко', 'Червоне'),
    ('Банан', 'Жовтий'),
    ('Апельсин', 'Помаранчевий')
])
conn.commit()


cursor.execute('''
UPDATE Fruits
SET Колір = 'Зелене' 
WHERE Назва_фрукта = 'Яблуко' 
''')
conn.commit()

print("Фрукти жовтого кольору:")
cursor.execute('''
SELECT ID, Назва_фрукта, Колір 
FROM Fruits 
WHERE Колір = 'Жовтий' -- Вибираємо лише жовті фрукти
''')
yellow_fruits = cursor.fetchall()
for fruit in yellow_fruits:
    print(f"ID: {fruit[0]}, Назва фрукта: {fruit[1]}, Колір: {fruit[2]}")

print("\nВсі записи про фрукти:")
cursor.execute('''
SELECT ID, Назва_фрукта, Колір 
FROM Fruits 
''')
all_fruits = cursor.fetchall()
for fruit in all_fruits:
    print(f"ID: {fruit[0]}, Назва фрукта: {fruit[1]}, Колір: {fruit[2]}")

conn.close()
