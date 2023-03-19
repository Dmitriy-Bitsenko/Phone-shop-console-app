import psycopg2

connection = psycopg2.connect(
    database="phone_store",
    user="postgres",
    password="z",
    host="localhost",
    port="5432"
)
print(f' {connection}, \n "Соединение установлено" ')

cursor = connection.cursor()


# create_users = """
# CREATE TABLE IF NOT EXISTS users (
#     id serial NOT NULL,
#     last_name varchar(50) NOT NULL,
#     first_name varchar(50) NOT NULL,
#     patronymic varchar(50) NOT NULL,
#     login varchar(20) NOT NULL,
#     password varchar(30) NOT NULL,
#     character varchar(30) DEFAULT 'user'
# );
# """
#
# cursor.execute(create_users)
# connection.commit()
# cursor.close()
# connection.close()


# add_users = """
# INSERT INTO users (last_name, first_name, patronymic, login, password) VALUES
# ('Иванов', 'Иван', 'Иванович', 'admin', 'admin'),
# ('Петрова', 'Анна', 'Васильевна', 'anna', 'anna'),
# ('Утро', 'Владимир', 'Петрович', '123', '123'),
# ('Печкин', 'Николай', 'Сидорович', 'mail', '1q2w');
# """
#
# cursor.execute(add_users)
# connection.commit()
# cursor.close()
# connection.close()


def list_users():
    cursor.execute('SELECT * FROM users')
    lst_users = cursor.fetchall()
    for user in lst_users:
        return lst_users


def list_login():
    cursor.execute('SELECT login FROM users')
    lst_login = cursor.fetchall()
    for login in lst_login:
        return lst_login


def list_password():
    cursor.execute('SELECT password FROM users')
    lst_password = cursor.fetchall()
    for password in lst_password:
        return lst_password


def character():
    cursor.execute('SELECT character FROM users')
    lst_character = cursor.fetchall()
    for role in lst_character:
        return lst_character


# cursor.execute()
# connection.commit()
# cursor.close()
# connection.close()


if __name__ == "__main__":
    print('Выполнение функции завершено', list_users())
    print('Выполнение функции завершено', list_login())
    print('Выполнение функции завершено', list_password())
    print('Выполнение функции завершено', character())
