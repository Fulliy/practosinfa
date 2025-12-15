##Задание 1
# from datetime import datetime

# def word():
#   days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#   date_time = datetime.now()
#   return days[date_time.weekday()]

# print(word())



## Задание 2
# from datetime import datetime

# def data(vvedite):
#   days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#   day_index = vvedite.weekday()
#   return days[day_index]

# today = datetime.now()
# print(data(today))


# #Задание 3
# def sec(seconds):
#   seconds_in_day = 24 * 60 * 60
#   return seconds / seconds_in_day

# vvod = input("Введите количество секунд: ")
# seconds = float(vvod)
# days = sec(seconds)
# print(f"{seconds} секунд = {days} суток")

# #Задание 4
# def chislo(dlinna, text):
#   if len(text) <= dlinna:
#     return text
#   else:
#     return text[:dlinna]

# print(chislo(10, "12345678910111213141516"))

#Задание 5
# def zz(month, day):

#     if (month == 3 and day == 21) or (month == 4 and day == 19):
#         return "Овен"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "телец"
#     elif (month == 5 and day == 21) or (month == 6 and day == 20):
#         return "Близнецы"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "рак"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "лев"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "дева"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "весы"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "скорпион"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "стрелец"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "козерог"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "водолей"
#     elif (month == 4 and day == 20) or (month == 5 and day == 20):
#         return "рыбы"
#     else:
#         return "Нет зз"

# print(zz(4,21))