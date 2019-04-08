# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:23:01 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import argparse


def insertion_sort_(lst=[6, 5, 3, 1, 8, 7, 2, 4]):
    lst_sorted = [lst[0]]
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if lst_sorted[j] < lst[i]:
                lst_sorted.insert(j+1, lst[i])
                break
        else:
            lst_sorted.insert(0, lst[i])
    return lst_sorted


def insertion_sort(lst=[6, 5, 3, 1, 8, 7, 2, 4]):
    n = len(lst)
    if n < 2:
        return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst


def main(lst):
    print(f'original list:{lst}',
          f'my version:{insertion_sort_(lst)}',
          f'pretty version:{insertion_sort(lst)}',
          sep='\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list',
                        nargs='+',
                        default=[6, 5, 3, 1, 8, 7, 2, 4],
                        type=int)
    args = parser.parse_args()
    main(args.list)
