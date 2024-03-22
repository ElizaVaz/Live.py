import time
len_world = input("Длина 'мира': ")
while not len_world.isdigit():  # Проверка что ввели число
    print("Это не число. Введите ЧИСЛО.")
    len_world = input("Длина 'мира': ")
len_world = int(len_world)

n_print = input("Количество поколений: ")
while not n_print.isdigit():  # Проверка что ввели число
    print("Это не число. Введите ЧИСЛО.")
    n_print = input("Длина 'мира': ")
n_print = int(n_print)

world = ["o"] * len_world
