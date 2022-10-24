# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
value = int(59)  # Кол-во конфет

search = int(input(f"Выберите 2го игрока:\n 1 = человек\n 2 = бот (если ходит первым, у вас нет шансов)\n "))
pl = 0
while search < 1 or search > 2:
    search = int(input(f"Введите корректное значение: "))
if search == 1:
    pl = 1
    sq = "Игрок 2"
if search == 2:
    pl = 2
    sq = "Bot"
print("Количество конфет: ", value)
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_calc(value):
    k = value % 29
    if k == 0:
        k = randint(1,28)
    return k
player1 = "Игрок 1"
player2 = sq
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
counter1 = 0 
counter2 = 0

if pl == 1:
    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)

        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)
else:
    while value > 28:
        if flag:
            k = input_dat(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)

        else:
            k = bot_calc(value)
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)
if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")