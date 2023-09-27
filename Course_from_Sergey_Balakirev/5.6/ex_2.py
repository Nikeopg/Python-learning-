import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for row in range(len(lst_in)):
    while lst_in[row].count(" ") > 0 or lst_in[row].count("--") > 0:
        lst_in[row] = lst_in[row].replace(" ", "-")
        lst_in[row] = lst_in[row].replace("--", "-")
    print(lst_in[row], end='\n')