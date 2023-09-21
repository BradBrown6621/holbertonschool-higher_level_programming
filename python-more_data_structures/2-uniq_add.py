#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return []
    uniqs = []
    for target in my_list:
        if target not in uniqs:
            uniqs.append(target)
    return sum(uniqs)
