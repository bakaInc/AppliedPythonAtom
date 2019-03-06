#!/usr/bin/env python
# coding: utf-8
'''
Простенький калькулятор в прямом смысле. Работает c числами
:param x: первый агрумент
:param y: второй аргумент
:param operator: 4 оператора: plus, minus, mult, divide
:return: результат операции или None, если операция не выполнима
'''


def calculator(x, y, operator):
    try:
        int(x)
        int(y)
        result = {
            'plus': lambda x, y: (x + y),
            'minus': lambda x, y: (x - y),
            'mult': lambda x, y: float(x * y),
            'divide': lambda x, y: (x / y),
        }.get(operator, None)
        return result(x, y)
    except:
        return None
