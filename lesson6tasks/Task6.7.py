'''
Реализовать функцию, которая создаёт матрицу
размером M строк на N столбцов и заполняет её рандомными
числами.
'''
import numpy as np
def create_random_matrix(m, n):
    return np.random.rand(m, n)
print('Введите количество строк m: ')
m = int(input())
print('Введите количество столбцов n: ')
n = int(input())
random_matrix = create_random_matrix(m, n)
print("Случайная матрица размером {}x{}:\n{}".format(m, n, random_matrix))
