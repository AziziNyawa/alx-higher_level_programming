#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_in_list = set(my_list)
    num = 0

    for i in uniq_in_list:
        num += i

    return (num)
