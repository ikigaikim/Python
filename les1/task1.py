# a = 10
# b = 10
# print (a)

while True:
    usr_input = input("Сколько вам лет?\n")
    if usr_input.isdigit():
        print("Здорово")
        break
    else:
        print("Введите сколько вам лет")
