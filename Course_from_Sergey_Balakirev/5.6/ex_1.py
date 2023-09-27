N = int(input())

# Создание двумерного списка
my_list = [[1] * (N-1) + [5] for _ in range(N)]

# Вывод списка в виде таблицы чисел
for row in my_list:
    print(*row)