#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    dim = len(list_of_lists)
    det = 0
    sign = 1
    i = 0
    for j in range(dim):
        if len(list_of_lists[i]) != dim:
            return None
        minors = []
        for k in range(dim - 1):
            minors.append([])
            for m in range(dim):
                if m != j:
                    minors[k].append(list_of_lists[k + 1][m])

        det += sign * list_of_lists[i][j] * \
               (calculate_determinant(minors) or 1)
        sign = -sign

    return det
