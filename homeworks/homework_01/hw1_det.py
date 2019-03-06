#!/usr/bin/env python
# coding: utf-8

'''
Метод, считающий детерминант входной матрицы,
если это возможно, если невозможно, то возвращается
None
Гарантируется, что в матрице float
:param list_of_lists: список списков - исходная матрица
:return: значение определителя или None
'''

def calculate_determinant(list_of_lists):
    det=0
    x = len(list_of_lists)
    sign = 1
    ind = 0
    for y in range(x):
        if len(list_of_lists[ind]) != x:
            return None
        ms = []
        for k in range(x - 1):
            ms.append([])
            for m in range(x):
                if m != y:
                    ms[k].append(list_of_lists[k + 1][m])

        det += sign * list_of_lists[ind][y] * (calculate_determinant(ms) or 1)
        sign = -sign

    return det
