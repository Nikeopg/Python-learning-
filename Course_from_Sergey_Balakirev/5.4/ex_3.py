"""
Большой подвиг 3. В виде строки записано арифметическое выражение, например:
"10 + 25 - 12"
или
"10 + 25 - 12 + 20 - 1 + 3"
и т. д. То есть, количество действий может быть разным.
Необходимо выполнить вычисление и результат отобразить на экране. Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа. Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
Sample Input:
10+25 - 12
Sample Output:
23
"""


expression = input("Введите арифметическое выражение: ")
expression = expression.replace(" ", "")

result = 0
current_number = ""

for char in expression:
    if char.isdigit():
        current_number += char
    else:
        if current_number:
            if expression.index(char) == 0 or expression[expression.index(char)-1].isdigit():
                result += int(current_number)
            else:
                result -= int(current_number)
            current_number = ""

if current_number:
    result += int(current_number)

print("Результат:", result)