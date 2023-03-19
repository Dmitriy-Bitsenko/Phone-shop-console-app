import psycopg2
import db_phones as db_phones
import db_users as db_users

connection = psycopg2.connect(
    database="phone_store",
    user="postgres",
    password="z",
    host="localhost",
    port="5432"
)
print(f' {connection}, \n "Соединение установлено" ')
cursor = connection.cursor()

check_login = db_users.list_login()
check_password = db_users.list_password()
check_users = db_users.list_users()
show_phone = db_phones.show_phones()
check_character = db_users.character()

# add_phones = db_phones.add_phones()
# print("ALL CHARACTERS: ", check_character)  #  ========== работает
# print("Вывод списка телефонов: ", show_phone) #  ====== работает
# print("Вывод списка логинов: ", check_login)  # ====== работает
# print("Вывод всех пользователей: ", check_users) #  ====== работает
# print("Вывод логина и пароля: ", check_login[2], check_password[2]) ===== работает
# print("Данные пользователя: ", check_users[2]) ===== работает


def add_user(last_name, first_name, patronymic, login, password):
    cursor.execute(
        "INSERT INTO users (last_name, first_name, patronymic, login, password) VALUES (%s,%s,%s,%s,%s)",
        (last_name, first_name, patronymic, login, password)
    )
    connection.commit()
    print("Вы зарегистрированы!")
    return True


def get_user(login: str, password: str):
    """Проверяет логин и пароль пользователя"""
    for i in check_login:
        if login in i:
            return True
        for p in check_password:
            if password in p:
                return True
    else:
        return False


def add_phone(title, memory, ram, cpu):
    cursor.execute("INSERT INTO phones (title, memory, ram, cpu) VALUES (%s,%s,%s,%s)",
                   (title, memory, ram, cpu)
)
    connection.commit()
    print("Товар успешно добавлен!")
    return True


def remove_phone():
    cursor.execute(f"DELETE FROM phones WHERE id={remove__}")
    connection.commit()
    print("Товар успешно удалён!")
    return True


while True:
    print('''Выберите пункт меню:
    a - Aвторизоваться
    r - Зарегистрироваться
    ''')

    user_input = input()
    if user_input == 'a':
        print('Введите логин:')
        login = input()
        print('Введите пароль:')
        password = input()
        result = get_user(login, password)

        if result:
            if login == 'admin':
                print("Список пользователей  - С, Перечень телефонов - T, Добавить пользователя - U,"
                      " Добавить товар - P, Удалить товар - D")
                admin_input = input()
                if admin_input == 'C':
                    for i in check_users:
                        print(*i)
                if admin_input == 'T':
                    for i in show_phone:
                        print(*i)
                if admin_input == 'U':
                    print('Введите фамилию пользователя:')
                    last_name = input()
                    print('Введите имя:')
                    first_name = input()
                    print('Введите отчество:')
                    patronymic = input()
                    print('Введите логин:')
                    login = input()
                    print('Введите пароль:')
                    password = input()
                    print('Повторите пароль:')
                    password_repeat = input()
                    result = add_user(last_name, first_name, patronymic, login, password)

                if admin_input == 'P':
                    print("Введите наименование:")
                    title = input()
                    print("Введите объём памяти:")
                    memory = input()
                    print("Введите озу:")
                    ram = input()
                    print("Введите наименование процессора:")
                    cpu = input()
                    result = add_phone(title, memory, ram, cpu)
                try:
                    if admin_input == 'D':
                        print("Введите id телефона:")
                        remove__ = int(input())
                        result = remove_phone()
                except:
                    print("Введите цифровое значение")

            if login != 'admin':
                print('Вы вошли в систему. Хотите посмотреть перечень телефонов?')
                print('Y - да'',', 'N - нет')
                user_input2 = input()
                if user_input2 == 'Y':
                    for i in show_phone:
                        print(*i)
                if user_input2 == 'N':
                    print('До встречи!')
                break  # Выходим из цикла
        else:
            print('Неверный логин или пароль')

    elif user_input == 'r':
        print('Введите фамилию:')
        last_name = input()
        print('Введите имя:')
        first_name = input()
        print('Введите отчество:')
        patronymic = input()
        print('Введите логин:')
        login = input()
        print('Введите пароль:')
        password = input()
        print('Повторите пароль:')
        password_repeat = input()

        if password != password_repeat:
            print('Пароли не совпадают!')
            continue
        result = add_user(last_name, first_name, patronymic, login, password)

    elif user_input != 'a' or 'r':
        print('Завершение работы')
        break  # Выходим из цикла
