import sqlite3


def read_db():
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('db.sqlite3') as con:
        # Создаем курсор для выполнения запросов
        cur = con.cursor()

        cur.execute('''
                    SELECT *
                    FROM test_1_worker
                    ''')

        rows = cur.fetchall()
        for i in rows:
            print(f"id: {i[0]}\nname: {i[1]}\nsurname: {i[2]}\nsalary: {i[3]}")
            print()


def write_to_db():
    with sqlite3.connect('db.sqlite3') as con:
        cur = con.cursor()

        # Здесь могут быть любые данные, без id
        data = ['Марк', 'Ефремов', '15000']
        # Чтобы никаких конфликтов не было надо прописывать что мы добавляем
        # А именно name, surname, salary
        # Иначе sql будет ругаться на то что ему дали недостаточно значений
        cur.execute(
            "INSERT INTO test_1_worker (name, surname, salary) VALUES (?,?,?);", data)

        rows = cur.fetchall()
        for i in rows:
            print(f"id: {i[0]}\nname: {i[1]}\nsurname: {i[2]}\nsalary: {i[3]}")
            print()


# read_db()
write_to_db()
