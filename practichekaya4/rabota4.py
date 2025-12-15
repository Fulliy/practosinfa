import csv
import json

test_csv = [
    ['Животное', 'Среда обитания'],
    ['Медведь', 'Лес'],
    ['Дельфин', 'Океан'],
    ['Верблюд', 'Пустыня']
]

with open('animals', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_csv)

with open('zoo_json', 'w', encoding='utf-8') as jsonfile:
    with open('animals', 'r', newline='', encoding='utf-8') as csvfile:
        json.dump(list(csv.DictReader(csvfile)), jsonfile, ensure_ascii=False, indent=4)
