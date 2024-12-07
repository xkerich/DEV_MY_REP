'''
Программа получает на вход число. Реализовать
функцию, которая определяет, является ли это число простым
(делится только на единицу и на само себя).
'''
import math
def prime_number_or_not(n):
    if n <= 1:
        return False
    for i in range(2, int(math.pow(n,0.5)) + 1):
        if n % i == 0:
            return False
        return True
print('Введите число: ')
number = int(input())
if prime_number_or_not(number):
    print(f'{number} - Простое число')
else:
    print(f'{number} - Не простое число')