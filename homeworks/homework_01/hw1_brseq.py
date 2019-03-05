#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
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
        if (not (
                (openingBracket == '(' and elem == ')') or
                (openingBracket == '[' and elem == ']') or
                (openingBracket == '{' and elem == '}')
                )):
            return False
    if len(stack) != 0:
        return False
    return True
