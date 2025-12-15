import csv
import os

def pereborka(csv_file_name):
    if not os.path.exists(csv_file_name):
        print("Файл не найден.")
        return

    with open(csv_file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if 'Возраст' in row:
                age_em = row['Возраст']

            try:
                age = int(row['Возраст']) 
                if age > 30:
                    print(row['Имя'])
            except ValueError:
                continue

temp_csv_data = [
    ['Имя', 'Возраст', 'Город', 'Должность'],
    ['Иван', '28', 'Москва', 'Инженер'],
    ['Анна', '35', 'Санкт-Петербург', 'Менеджер'],
    ['Петр', '42', 'Новосибирск', 'Директор'],
    ['Мария', '29', 'Казань', 'Разработчик'],
    ['Ольга', 'тридцать', 'Екатеринбург', 'Аналитик'],
    ['Сергей', '31', 'Воронеж', 'Специалист'],
    ['Елена', '30', 'Омск', 'Бухгалтер']
]

with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(temp_csv_data)

pereborka('employees.csv')

pereborka('non_existent_file.csv')