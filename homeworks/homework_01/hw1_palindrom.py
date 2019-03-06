#!/usr/bin/env python
# coding: utf-8

'''
Метод проверяющий строку на то, является ли она палиндромом.
:param input_string: строка
:return: True, если строка являестя палиндромом
False иначе
'''

def invertInt(x):
    return (int)(str(x)[::-1])

def check_palindrom(x):
    if x == invertInt(x):
        return True
    else:
        return False
