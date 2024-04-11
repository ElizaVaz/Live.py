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
        world_x.append("■")
    else:
        world_x.append(" ")
world = world_x

print("".join([x for x in world]))


def klet_live(i):
    ret = 1
    if i == 0:
        if world[-1] == world[i + 1]:
            ret = 0
    elif i == len(world) - 1:
        if world[i - 1] == world[0]:
            ret = 0
    else:
        if world[i - 1] == world[i + 1]:
            ret = 0
    return ret


def klet_die(i):
    ret = 0
    if i == 0:
        if world[-1] != world[i + 1]:
            ret = 1
    elif i == len(world) - 1:
        if world[i - 1] != world[0]:
            ret = 1
    else:
        if world[i - 1] != world[i + 1]:
            ret = 1
    return ret


for n in range(n_print):
    new_world = world.copy()
    for i in range(len(world)):
        if world[i] == "■":
            live = klet_live(i)
            if live == 0:
                new_world[i] = " "
        else:
            live = klet_die(i)
            if live == 1:
                new_world[i] = "■"
    world = new_world
    print("".join([x for x in world]))
    time.sleep(0.5)

input()
