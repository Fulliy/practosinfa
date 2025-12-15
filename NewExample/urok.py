file = open('example.txt', 'w')
file.write("Привет мир")
file.close()

# Режим «w» используется для открытия файла на запись. Если файл с таким именем существует, он будет очищен перед записью
with open('text.txt', 'w', encoding='utf-8') as file:
   file.write(f'Привет мир \n')
# Режим «a» также открывает файл на запись, но в отличие от режима «w», он добавляет данные в конец файла, не удаляя существующие.
with open('text.txt', 'a', encoding='utf-8') as file:
    file.write(f'Привет андрей \n')
# режим чтения
with open('text.txt', 'r', encoding='utf-8') as file:
    conent=file.read()
    print(conent)


with open('text.txt', 'r', encoding='utf-8') as file:
    line1=file.readline()
    line2=file.readline()
    line3=file.readline()
    print('построчное чтение')
    print(f'первая строка {line1.strip()}')
    print(f'вторая строка {line2.strip()}')
    print(f'третья строка {line3.strip()}')


# особ чтения файла построчно.
with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())


# считывает все строки файла и возвращает их в виде списка строк, где каждый элемент списка – это одна строка из файл
with open('text.txt', 'r', encoding='utf-8') as file:
    data=file.readlines()
    for i, line in enumerate(data, 1):
        print(f'строка {i} : {line.strip()}')


# способ получить все строки файла в виде списка.
with open('text.txt', 'r', encoding='utf-8') as file:
    data=list(file)
    print(data)


with open('test.txt','r+',encoding ='utf-8') as file:
    file.write('Как дела?\n')
    line = ['маша\n','коля\n','миша\n']
    file.writelines(line)
                
# очистка файла
import os
if os.path.exists('text.txt'):
    os.remove('text.txt')


# чтение файла
with open('text.txt', 'r', encoding='utf-8') as file:
    result=file.read()
    print(result)


# Этот блок демонстрирует безопасное открытие файла с использованием конструкции
try:
    with open('example.txt','r') as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print('Файл не найден')
except PermissionError:
    print('Нет прав доступа к файлу')
finally:
    print('Работа c файлом завершена')

# # Режим «r+» открывает файл на чтение и запись. Но в отличие от режимов «w+» и «a+», 
# # файл не будет создан, если он не существует, и запись будет производиться с начала файла, без очистки существующих данных.
with open('text.txt', 'r+', encoding='cp1251') as file: 
    #чтобы прочитать 5 символ 
    file.write('1234567890asdfg')
    file.read(5)
    data=file.read(1)
    print(data)



#чтобы прочитать 4 символ с конца
with open ('text.txt','r+b') as file:
    file.write(b'1234567890asdfg')
    file.seek(-4,2)
    data = file.read(1)
print(data)


#сколько байтов занимает 
with open ('text.txt','r+') as file:
    file.write('1234567890asdfg')
    file.read(5)
    content = file.tell()
print(content)











# # # Задача 1: "Дневник настроения"

# # # Условие: Напишите программу, которая будет записывать в файл 
# # # ваше настроение каждый день. Программа должна спрашивать у 
# # # пользователя, какое у него сегодня настроение, и сохранять его в 
# # # файл с текущей датой.

# # from datetime import datetime 

# # def nast():
# #     mood = input('Какое у тебя сегодня настроение?')
# #     date_time = datetime.now()
# #     date_str = date_time.strftime("%d.%m.%Y,  %H: %M: %S")

# #     with open('file.txt','a',encoding='utf-8') as file_n:
# #         m=f"[{date_str}] Настроение: {mood}\n"
# #         file_n.write(m)
# #     print('Настроение сегодня')
# # nast()


# # # Задача 2: "Читатель цитат"

# # # Условие: Создайте программу, которая читает файл с цитатами и 
# # # показывает случайную цитату пользователю. 
# # # Если файла не существует, программа создает его с примером цитат.

# # import random
# # import os

# # def reader():
# #     filename = 'quotes.txt'
    
# #     if not os.path.exists(filename):
# #         with open(filename, 'w', encoding='utf-8') as file:
# #             file.write("Жизнь — это то, что происходит с тобой, пока ты строишь другие планы.\n")
# #             file.write("Единственный способ сделать великую работу — любить то, что ты делаешь.\n")
# #             file.write("Будь тем изменением, которое ты хочешь видеть в мире.\n")
# #         print("Файл с цитатами создан!")
    
# #     try:
# #         with open(filename, 'r', encoding='utf-8') as file:
# #             quotes = [line.strip() for line in file if line.strip()]
        
# #         if quotes:
# #             random_quote = random.choice(quotes)
# #             print(f"Случайная цитата: {random_quote}")
# #         else:
# #             print("Файл с цитатами пуст.")
            
# #     except Exception as e:
# #         print(f"Ошибка: {e}")

# # reader()
