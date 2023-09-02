# 1)
f, s = map(int, input().split())
while f <= s:
    print(f ** 2, end=" ")
    f += 1

# 2)
book_price = float(input())
i = 2
while i <= 10:
    print(round(book_price * i,1), end=' ')
    i += 1

# 3)
num = int(input())
i, sum = 2, 1
while i <= num:
    sum += 1/i
    i+=1
print(round(sum,3))


'''
1) Вводятся два целых положительных числа n и m, причем, n < m. Вывести в строку через пробел квадраты целых чисел в
диапазоне [n; m]. Программу реализовать при помощи цикла while.
Sample Input:
2 4
Sample Output:
4 9 16

2) Вводится стоимость одной книги x рублей (вещественное число).
Необходимо вывести на экран в строчку через пробел стоимости 2, 3, ... 10 таких книг с точностью до десятых. Программу реализовать при помощи цикла while.
Sample Input:
34.6
Sample Output:
69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0

3) Вводится целое положительное число n. Вычислить и вывести на экран сумму: 1 + 1/2 + 1/3 + ... + 1/n с точностью до тысячных (три знака после запятой).
Программу реализовать при помощи цикла while.

Sample Input:
8
Sample Output:
2.718
'''
