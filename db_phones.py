import psycopg2

connection = psycopg2.connect(
    database="phone_store",
    user="postgres",
    password="z",
    host="localhost",
    port="5432"
)
print(f'{connection}, \n "Соединение установлено" ')

cursor = connection.cursor()

create_phones = """
CREATE TABLE IF NOT EXISTS phones (
    id serial NOT NULL,
    title varchar(50) NOT NULL,
    memory varchar(20) NOT NULL,
    ram varchar(30) NOT NULL,
    cpu varchar(50) NOT NULL
);
"""
add_phones = """
INSERT INTO phones (title, memory, ram, cpu) VALUES
('Nokia C01 Plus', '16Gb', '1Gb', '4x Cortex-A55 1.6 ГГц'),
('Apple iPhone 11', '64Gb', '4Gb', '2x Lightning 2.65 ГГц'),
('Black Fox B2', '8Gb', '1Gb', '4x Cortex-A7 1.3 ГГц'),
('Samsung Galaxy A52', '256Gb', '8Gb', '2x Kryo 465 (Cortex-A76)'),
('Xiaomi Redmi Note 10 Pro', '128Gb', '8Gb', '6x Kryo 470 (Cortex-A55)');
"""


def show_phones():
    cursor.execute('SELECT * FROM phones')
    show = cursor.fetchall()
    for phone in show:
        return show


# # cursor.execute()
# connection.commit()
# cursor.close()
# connection.close()


if __name__ == "__main__":
    show_phones()


