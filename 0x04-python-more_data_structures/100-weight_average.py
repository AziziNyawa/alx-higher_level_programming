#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        deno = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            deno += (tup[1])
        return (num/deno)
    return 0
