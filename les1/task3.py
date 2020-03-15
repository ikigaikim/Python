# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    usr_input = input("Введите число\n")

    if usr_input.isdigit():
        result = int(usr_input) + int(usr_input * 2) +int(usr_input * 3)
        break
    else:
        print ("Введено не число")
print(f'n + nn + nnn = {result}')