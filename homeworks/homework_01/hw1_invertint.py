#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    number_str = str(number)
    return -int(number_str[:0:-1]) if number_str[0] == \
        '-' else int(number_str[::-1])
