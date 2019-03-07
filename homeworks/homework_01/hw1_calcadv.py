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
    raise NotImplementedError
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
    if not is_bracket_correct(input_string):
        return None

    while " -" in input_string:
        input_string = input_string.replace(" -", "-")
    while " +" in input_string:
        input_string = input_string.replace(" +", "+")
    while " /" in input_string:
        input_string = input_string.replace(" *", "*")
    while " /" in input_string:
        input_string = input_string.replace(" /", "/")

    while "- " in input_string:
        input_string = input_string.replace("- ", "-")
    while "+ " in input_string:
        input_string = input_string.replace("+ ", "+")
    while "* " in input_string:
        input_string = input_string.replace("* ", "*")
    while "/ " in input_string:
        input_string = input_string.replace("/ ", "/")
    while "--" in input_string:
        input_string = input_string.replace("--", "-")
    while "++" in input_string:
        input_string = input_string.replace("++", "+")
    while "+-" in input_string:
        input_string = input_string.replace("+-", "-")
    while "**" in input_string:
        return None
    while "//" in input_string:
        return None
    while "(-" in input_string:
        input_string = input_string.replace("(-", "(0-")
    while "/-" in input_string:
        input_string = input_string.replace("/-", "*(0-1)/")
    while "*-" in input_string:
        input_string = input_string.replace("*-", "*(0-1)*")
    while "*+" in input_string:
        input_string = input_string.replace("*+", "*(0+1)*")

    if len(input_string) > 0:
        if input_string[0] is "-" or input_string[0] is "+":
            input_string = "0" + input_string
        if input_string[0] is "*" or input_string[0] is "/":
            return None

    res = []
    opers = []
    operators = {'+': 2, '-': 2, '*': 1, '/': 1}

    input_string = splitArr(input_string)
    old = ""
    try:
        for ch in input_string:
            tt = ch
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
            elif opers \
                    and opers[-1] != '(':
                if operators.get(opers[-1]) <= operators.get(ch):
                    res.append(opers.pop())
                    opers.append(ch)
                else:
                    opers.append(ch)
            else:
                opers.append(ch)
            if (old is ')' and tt.isdigit()) or (old.isdigit() and tt is '('):
                return None

            old = tt
        if len(res) < 1:
            return None
        while opers:
            res.append(opers.pop())

        for el in res:
            if el.isdigit():
                opers.append(el)
            else:
                d2 = float(opers.pop())
                d1 = float(opers.pop())

                if el == '+':
                    opers.append(d1 + d2)
                if el == '-':
                    opers.append(d1 - d2)
                if el == '*':
                    opers.append(d1 * d2)
                if el == '/':
                    opers.append(d1 / d2)

    except:
        return None

    if len(opers) == 1:
        return float(opers[0])
    else:
        return None
