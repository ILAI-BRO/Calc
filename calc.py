def get_num(promp):
    while True:
        value = input(promp)
        if value.lstrip("-").isdigit():
            return int(value)
        else:
            print("Пожалуйста введите целое число!")

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: "Ошибка деление на ноль" if y == 0 else x / y

# def div(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return "Ошибка! Деление на ноль."
#     except TypeError:
#         return "Ошибка типа данных."

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

valid_choices = ['1', '2', '3', '4']

while True:
    choice = input("Введите номер операции (1-2-3-4): ")
    if choice in valid_choices:
        choice = int(choice)
        break
    print("Вы ввели неправильный номер операции!")

# valid_choices = ['1', '2', '3', '4']
# choice = None
# while choice not in valid_choices:
#     choice = int(input("Введите номер операции (1-2-3-4): "))
#     if choice not in valid_choices:
#         print("Вы ввели неправильный номер операции!")



num1 = get_num("Введите первое число: ")
num2 = get_num("Введите второе число: ")


if choice == 1:
    print(f"Результат сложения {num1} + {num2} = {add(num1, num2)}")
elif choice == 2:
    print(f"Результат вычитания {num1} - {num2} = {sub(num1, num2)}")
elif choice == 3:
    print(f"Результат умножения {num1} * {num2} = {mul(num1, num2)}")
elif choice == 4:
    result = div(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат деления {num1} / {num2} = {result:.2f}")

