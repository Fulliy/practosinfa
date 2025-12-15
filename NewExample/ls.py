def get_zodiac_sign(month, day):
    if not 1 <= month <= 12:
        return "Ошибка: Месяц должен быть от 1 до 12."
    
    if not 1 <= day <= 31:
        return "Ошибка: День должен быть от 1 до 31."

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Рыбы"
    else:
        return "Не удалось определить знак зодиака."


print(get_zodiac_sign(13, 15))
print(get_zodiac_sign(4, 31))
print(get_zodiac_sign(4, 32))

def sum_of_divisors(number):
  if not isinstance(number, int) or number <= 0:
    return "Ошибка: Введите положительное целое число."

  total_sum = 0
  for i in range(1, number + 1):
    if number % i == 0:
      total_sum += i
      
  return total_sum

print(f"Сумма делителей числа 6: {sum_of_divisors(6)}")
print(f"Сумма делителей числа 12: {sum_of_divisors(12)}")
print(f"Сумма делителей числа 7: {sum_of_divisors(7)}")
print(f"Сумма делителей числа 1: {sum_of_divisors(1)}")
print(f"Сумма делителей числа 0: {sum_of_divisors(0)}")
print(f"Сумма делителей числа -5: {sum_of_divisors(-5)}")
print(f"Сумма делителей числа 4.5: {sum_of_divisors(4.5)}")