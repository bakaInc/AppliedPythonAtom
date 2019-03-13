#!/usr/bin/env python
# coding: utf-8
'''
Метод проверяющий строку на то, является ли она палиндромом.
:param input_string: строка
:return: True, если строка являестя палиндромом
False иначе
'''


def check_palindrom(x):
    if x == x[::-1]:
        return True
    else:
        return False
