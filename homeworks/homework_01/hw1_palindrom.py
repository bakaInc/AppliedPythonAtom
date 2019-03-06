#!/usr/bin/env python
# coding: utf-8

'''
Метод проверяющий строку на то, является ли она палиндромом.
:param input_string: строка
:return: True, если строка являестя палиндромом
False иначе
'''

def reverse(n):
    return (lambda:int(str(n)[::-1]),lambda: -1*int(str(n)[:0:-1]))[n < 0]()

def check_palindrom(x):
    if x == reverse(x):
        return True
    else:
        return False

