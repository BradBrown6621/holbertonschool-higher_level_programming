#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    tuples = [a, b]
    tuple_added = [0, 0]
    for i in range(len(tuple_a)):
        a[i] = tuple_a[i]
    for i in range(len(tuple_b)):
        b[i] = tuple_b[i]
    tuple_added = [0, 0]
    for i in range(2):
        tuple_added[i] = tuples[0][i] + tuples[1][i]
    return tuple(tuple_added)
