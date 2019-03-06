#!/usr/bin/env python
# coding: utf-8

from random import randint as ri

'''
Метод, считающий детерминант входной матрицы,
если это возможно, если невозможно, то возвращается
None
Гарантируется, что в матрице float
:param list_of_lists: список списков - исходная матрица
:return: значение определителя или None
'''

def LUdecomp(mx):
    n = len(mx)
    det = 0
    l = [[0 for i in range(n)] for j in range(n)]
    u = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        # Upper Triangular
        for j in range(i, n):
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for k in range(i):
                sum += (l[i][k] * u[k][j])
            u[i][j] = mx[i][j] - sum

        # Lower Triangular
        for j in range(i, n):
            if (i == j):
                l[i][i] = 1;  # Diagonal as 1
            else:
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for k in range(i):
                    sum += (l[j][k] * u[k][i])

                # Evaluating L(k, i)
                l[j][i] = (mx[j][i] - sum) / u[i][i]

    return l, u

def calculate_determinant(n):
    mx = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(ri(1, 10))
        mx.append(row)
    return mx

