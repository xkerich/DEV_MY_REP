'''
Дан список чисел, отсортированных по возрастанию. На вход принимается значение,
равное одному из элементов списка. Реализовать функцию, выполняющую рекурсивный
алгоритм бинарного поиска, на выходе программа должна вывести позицию искомого
элемента в исходном списке.
'''

def binary_searh(mass, left, right, x):
    if right >= left:
        middle = (right + left) // 2
        if mass[middle] == x:
            return middle
        elif mass[middle] > x:
            return binary_searh(mass, left, middle - 1, x)
        else:
            return binary_searh(mass, middle + 1, right, x)
    else:
        return -1
mass = [5, 7, 12, 77, 89, 100, 101, 112]
print('Введите искомое число: ')
x = int(input())
result = binary_searh(mass, 0, len(mass)-1, x)
if result != -1:
    result = result+1
    print(f'Элемент найден на позиции {result}')
else:
    print('Элемент не найден в массиве')