#!/usr/bin/env python
# coding: utf-8

'''
Калькулятор на основе обратной польской записи.
Разрешенные операции: открытая скобка, закрытая скобка,
плюс, минус, умножить, делить
:param input_string: строка, содержащая выражение
:return: результат выполнение операции, если строка валидная - иначе None
'''


def is_bracket_correct(input_string):
    stack = []
    for elem in input_string:
        if elem not in set('({[)}]'):
            continue
        if elem in set('({['):
            stack.append(elem)
            continue
        if len(stack) == 0:
            return False
        openingBracket = stack.pop()
        if not (openingBracket == '(' and elem == ')'):
            return False
    if len(stack) != 0:
        return False
    return True


def splitArr(arr):
    arr = arr.split()
    delimeters = ['(', ')', '+', '-', '*', '/']

    newArr = []

    for tmp in arr:
        res = ""
        for ch in tmp:
            if ch.isdigit() or ch.isalpha() or ch is ".":
                res += ch
            elif ch in delimeters:
                newArr.append(res)
                newArr.append(ch)
                res = ""
        newArr.append(res)
    newArr = [value for value in newArr if value != '']
    return newArr


def advanced_calculator(input_string):
    raise NotImplementedError
