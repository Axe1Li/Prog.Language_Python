# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

coin = int(input("Введите колличество монет: "))

count = 0

for i in range(coin):
    side = random.randint(0,1)
    print(side)
    if side == 0:
        count += 1
print("Нужно перевернуть", count, "монет")