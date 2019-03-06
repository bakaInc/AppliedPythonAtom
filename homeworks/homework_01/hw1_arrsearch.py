#!/usr/bin/env python
# coding: utf-8


def find_indices(arr, x):
    '''
    Метод возвращает индексы двух различных элементов listа,
    таких, что сумма этих элементов равна n.
    В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''

    l = len(arr)
    left = 0
    right = l - 1
    arr.sort()

    while (left != right):
        sum = arr[left] + arr[right]
        if sum < x:
            left += 1
        elif sum > x:
            right -= 1
        else:
            return (left, right)

    return None
