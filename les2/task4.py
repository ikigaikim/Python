'''
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
'''

user_words = input()

for idx, word in enumerate(user_words.split(" "),1):
    print(f'{idx}:{word[:10]}')