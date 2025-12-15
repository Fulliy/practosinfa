import csv
test_csv = [
    ['Имя', 'Возраст', 'Город'],
    ['Анна', '30', 'Москва'],
    ['Пётр', '34', 'Москва']
]

with open('test_data_csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_csv)

with open('test_data_csv', 'w', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row_num, row in enumerate(reader, 1):
        print(f'Строка {row_num}: {row}')
        print(f'Строка {type(row)}')

# with open('test_data_csv', 'w', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for i in reader:
#         print(f'{i['Имя']}, Возраст {i['Возраст']}, Город: {i['Город']},')
#         print(f"Тип: {type(i)}")

# import json

# rest_json = {
#     'Имя':'Анна',
#     'Возраст':'30',
#     'город':'москва'
# }

# with open('test_data_json', 'w', encoding='utf-8') as file:
#     json.dump(rest_json, file, ensure_ascii=False,indent=2)