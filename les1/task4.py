#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    usr_input = input("Введите целое положительное число: ")
    if usr_input.isdigit():
        num = int(usr_input)
        result = 0
        while num:
            tmp = num % 10
            if tmp > result:
                result = tmp
            num //= 10
        break
    else:
        print ("Ошибка ввода")
print(result)