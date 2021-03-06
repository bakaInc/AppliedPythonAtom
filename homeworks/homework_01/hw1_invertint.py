#!/usr/bin/env python
# coding: utf-8
'''
Метод, принимающий на вход int и
возвращающий инвертированный int
:param number: исходное число
:return: инвертированное число
'''


def reverse(n):
    return (lambda: int(str(n)[::-1]), lambda: -1*int(str(n)[:0:-1]))[n < 0]()
