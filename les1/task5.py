Sales = int(input('Введите выручку: '))
Costs = int(input('Введите ваши расходы: '))

if Sales >=Costs:
    Margin = (Sales - Costs) / Sales
    print ("Рентабельность: " "%.0f%%" % (Margin * 100))
    People = int(input('Сколько сотрудников в Вашей компании: '))
    print("Валовая прибыль на 1 сотрудника составляет: " "%.2f единицы на сотрудника" %  ((Sales - Costs) / People))

else:
    print ("Вы закончили год с убытком")

