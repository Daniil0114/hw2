#             Задача 10: На столе лежат n монеток.# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.# Выведите минимальное количество монет, которые нужно перевернуть
import coins

coins_count = int(input('Введите число монет: '))
import random = [random.randint(0, 1)
                      for _ in range(coins_count)]
print(coins)
if coins.count(0) < coins.count(1):
    print(coins.count(0))
else:
    print(coins.count(1))
