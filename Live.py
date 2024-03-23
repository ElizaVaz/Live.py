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

print("Теперь введите изначальный мир.")
print("Если вы хотите чтобы в клетке не было жизни введите 0, иначе любую другую цыфру.")
while True:
    world = input("Введите 'изначальный мир': ")
    if len(world) != len_world:
        if len(world) < len_world:
            print("Не достаточно символов для мира...")
        else:
            print("Слишком много символов для мира...")
        continue
    if not world.isdigit():
        print(f"Ты уверен что здесь только цыфры {world}?")
        continue
    break

world_x = list()
for i in range(len_world):
    if world[i] == "0":
        world_x.append("o")
    else:
        world_x.append(" ")
world = world_x

print("ИЗНАЧАЛЬНЫЙ МИР:", "".join([x for x in world]))
