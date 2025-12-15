import csv
import os
import json

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

def convert_csv_to_json(csv_path: str, json_path: str):
    data = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    print(f"CSV-файл '{csv_path}' успешно прочитан.")

    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Успешно: Данные конвертированы и записаны в JSON-файл '{json_path}'.")

def convert_json_to_csv(json_path: str, csv_path: str):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(f"JSON-файл '{json_path}' успешно прочитан.")

    names = list(data[0].keys())

    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=names)
        writer.writeheader()
        writer.writerows(data)
    print(f"Успешно: Данные конвертированы и записаны в CSV-файл '{csv_path}'.")

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

convert_csv_to_json('employees.csv', 'employees.json')

convert_json_to_csv('employees.json', 'employees_from_json.csv')

for f in ['employees.csv', 'employees.json', 'employees_from_json.csv']:
    os.remove(f)
    print(f"Удален файл: '{f}'")