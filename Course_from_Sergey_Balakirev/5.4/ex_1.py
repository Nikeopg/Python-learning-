"""
Подвиг 1. Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке. Вывести в строку через пробелы найденные индексы. Если этот фрагмент ни разу не будет найден, то вывести значение -1.
Sample Input:
Барабанщик бил бой в барабан
Sample Output:
2 23
"""


s = input("Введите строку: ")
fragment = "ра"

indices = [str(i) for i in range(len(s)) if s[i:i+len(fragment)] == fragment]
if indices:
    print(" ".join(indices))
else:
    print("-1")