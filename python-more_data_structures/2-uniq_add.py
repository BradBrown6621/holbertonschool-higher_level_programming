#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqs = []
    for target in range(len(my_list)):
        for arrow in range(len(uniqs)):
            if my_list[target] == uniqs[arrow]:
                uniqs.append(target)
    return uniqs
