#!/usr/bin/env python
# coding: utf-8

'''
Калькулятор на основе обратной польской записи.
Разрешенные операции: открытая скобка, закрытая скобка,
плюс, минус, умножить, делить
:param input_string: строка, содержащая выражение
:return: результат выполнение операции, если строка валидная - иначе None
'''


def splitArr(arr):
    arr = arr.split()
    delimeters = ['(', ')', '+', '-', '*', '/']

    newArr = []

    for tmp in arr:
        res = ""
        for ch in tmp:
            if ch.isdigit() or ch.isalpha():
                res += ch
            elif ch in delimeters:
                newArr.append(res)
                newArr.append(ch)
                res = ""
        newArr.append(res)
    newArr = [value for value in newArr if value != '']
    return newArr


def advanced_calculator(expr):
    res = []
    opers = []
    operators = {'+': 2, '-': 2, '*': 1, '/': 1}

    expr = splitArr(expr)

    # FORM RES, OPERS
    for ch in expr:
        if ch.isalpha():
            return None
        if ch.isdigit():
            res.append(ch)
        elif ch == '(':
            opers.append(ch)
        elif ch == ')':
            while opers[-1] != '(':
                res.append(opers.pop())
            opers.pop()
        elif opers and opers[-1] != '(':
            print(opers)
            if operators.get(opers[-1]) <= operators.get(ch):
                res.append(opers.pop())
                opers.append(ch)
            else:
                opers.append(ch)
        else:
            opers.append(ch)
    if len(res)<1:
        return None
    while opers:
        res.append(opers.pop())


    # CALCULATIONS
    for el in res:
        if el.isdigit():
            opers.append(el)
        else:
            d2 = int(opers.pop())
            d1 = int(opers.pop())

            if el == '+':
                opers.append(d1 + d2)
            if el == '-':
                opers.append(d1 - d2)
            if el == '*':
                opers.append(d1 * d2)
            if el == '/':
                opers.append(d1 / d2)
    if len(opers) == 1:
        return opers[0]
    else:
        return None
