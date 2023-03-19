'''
import csv
import functools as ft


def read_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return ft.reduce(lambda c, i: c + int(i[1]), reader, 0)


response = read_csv('./data.csv')
print(response)
'''

import csv


def read_csv(path):
    with open(path, 'r') as f:
        return sum(int(r[1]) for r in csv.reader(f))


response = read_csv('./data.csv')
print(response)
