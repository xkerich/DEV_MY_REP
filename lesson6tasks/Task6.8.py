'''
Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести
в консоль индексы найденных элементов.
'''

import numpy as np

def find_min_max(matrix):

    min_index = np.unravel_index(np.argmin(matrix), matrix.shape)
    max_index = np.unravel_index(np.argmax(matrix), matrix.shape)

    min_value = matrix[min_index]
    max_value = matrix[max_index]

    print(f"Минимальный элемент: {min_value}, индекс: {min_index}")
    print(f"Максимальный элемент: {max_value}, индекс: {max_index}")

print('Введите количество строк матрицы m: ')
m = int(input())

print('Введите количество столбцов матрицы n: ')
n = int(input())

matrix = np.random.randint(1, 100, size=(m, n))
print('Матрица:\n', matrix)

find_min_max(matrix)