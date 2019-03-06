#!/usr/bin/env python
# coding: utf-8

'''
Функция которая разворачивает словарь
, т.е. каждому значению ставит в соответствие ключ.
:param source_dict: dict
:return: new_dict: dict
'''

def invertRec(value):
    res = []
    if isinstance(value, list) or isinstance(value, set):
        for ind in value:
            res += invertRec(ind)
    else:
        res.append(value)
    return res

def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return None
    new_dict = {}
    for key, value in source_dict.items():
        for ind in invertRec(value):
            if ind in new_dict:
                if isinstance(new_dict[ind], list):
                    new_dict[ind].append(key)
                else:
                    item = new_dict.get(ind)
                    new_dict[ind] = [item, key]
            else:
                new_dict[ind] = key
    return new_dict
