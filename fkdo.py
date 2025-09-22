def calculator():
    print("Доступные операции:")
    print("1. Арифметические операторы")
    print("2. Операторы сравнения")
    print("3. Логические операторы")
    print("4. Операторы принадлежности")
    print("5. Операторы тождественности")

    operation_type = input("Введите тип операции (1-5): ")

    if operation_type == '1':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите оператор (+, -, *, /, //, %, **): ")

        if operation == '+':
            print(a + b)
        elif operation == '-':
            print(a - b)
        elif operation == '*':
            print(a * b)
        elif operation == '/':
            print(a / b)
        elif operation == '//':
            print(a // b)
        elif operation == '%':
            print(a % b)
        elif operation == '**':
            print(a ** b)
        else:
            print("Неверный оператор.")



    elif operation_type == '2':
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите оператор (==, !=, >, <, >=, <=): ")

        if operation == '==':
            print(a == b)
        elif operation == '!=':
            print(a != b)
        elif operation == '>':
            print(a > b)
        elif operation == '<':
            print(a < b)
        elif operation == '>=':
            print(a >= b)
        elif operation == '<=':
            print(a <= b)
        else:
            print("Неверный оператор.")
            


    elif operation_type == '3':
        a = bool(input("Введите первое логическое значение (True/False): "))
        b = bool(input("Введите второе логическое значение (True/False): "))
        operation = input("Введите логический оператор (and, or, not): ")

        if operation == 'and':
            print(a and b)
        elif operation == 'or':
            print(a or b)
        elif operation == 'not':
            num3 = int(input("Введите число для оператора not: "))
            if num3 == 0:
                result = True
            else: 
                result = False
        else:
            print("Неверный оператор.")



    elif operation_type == '4':
        container = input("Введите числа (например, '1, 2, 3' ): ").split()
        operation = input("Введите оператор (in, not in): ")

        if operation == 'in':
            container = [int(n) for n in container]
            a = int(input("Введите число, которое нужно проверить: "))
            if a in container:
                print(f"Число {a} есть в списке")
            else:
                print(f"Числа {a} нет в списке")
            print(a in container)
        elif operation == 'not in':
            container = [int(n) for n in container]
            b = int(input("Введите число, которое нужно проверить: "))
            if b not in container:
                print(f"Числа {b} нет в списке")
            else:
                print(f"Число {b} есть в списке")
            print(a not in container)
        else:
            print("Неверный оператор.")



    elif operation_type == '5':
        a = input("Введите первый объект: ")
        b = input("Введите второй объект: ")
        operation = input("Введите оператор (is, is not): ")

        if operation == 'is':
            print(a is b)
        elif operation == 'is not':
            print(a is not b)
        else:
            print("Неверный оператор.")

    else:
        print("Неверный тип операции.")

calculator()