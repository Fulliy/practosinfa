# students = [
#     {"name": "Alice", "grades": [85, 92, 78]},
#     {"name": "Bob", "grades": [65, 70, 80]},
#     {"name": "Charlie", "grades": [95, 88, 92]}
# ]

# def calculate_average(grades):
#     return sum(grades) / len(grades)

# for student in students:
#     student["average_grade"] = calculate_average(student["grades"])

# vishe = list(filter(lambda student: student["average_grade"] > 80, students))

# print("Лучшие студенты (средний балл выше 80):")
# for student in vishe:
#     print(f"- {student['name']}: {student['average_grade']:.2f}") 


from functools import reduce

numbers = [1,2,3,4,5]

def ab(x):
    return x*2
result = map(ab,numbers)
print(list(result))

add=map(lambda x: x*2 ,numbers)
print(list(add))



def ch(x):
    return x % 2 ==0
result = filter (ch,numbers)
print(list(result))

filt = filter(lambda x: x%2==0,numbers)
print(list(filt))

def add(x,y):
    return x+y
result = reduce(add,numbers)
print(result)

list1=[1,2,3,4,5]
list2 =['a','b','c','d','e']
result = zip(list1,list2)
print(list(result))


# lambda аргументы: выражение 

add=lambda x,y:x+y
print(add(5,6))


people= [("мария",34),("анастасия",23),("артем",7)]
sorted_people = sorted(people,key=lambda people: [0])
list.reverse(sorted_people)
print(list(sorted_people))


students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [65, 70, 80]},
    {"name": "Charlie", "grades": [95, 88, 92]}
]

def calculate_average(grades):
    return sum(grades) / len(grades)

# Список студентов
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [65, 70, 80]},
    {"name": "Charlie", "grades": [95, 88, 92]}
]

# Используем filter() с лямбда-функцией
best_students = filter(
    lambda student: calculate_average(student["grades"]) > 80, 
    students
)

# Выводим имена лучших студентов и их средний балл
print("Лучшие студенты:")
for student in best_students:
    avg_grade = calculate_average(student["grades"])
    print(f"{student['name']}: средний балл {avg_grade:.2f}")
