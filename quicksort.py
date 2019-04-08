# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:04:59 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import argparse


def quicksort_(lst=[3, 7, 8, 5, 2, 1, 9, 5, 4]):
    def partition(lst):
        less = []
        greater = []
        for e in lst[1:]:
            if e < lst[0]:
                less.append(e)
            else:
                greater.append(e)
        return less, [lst[0]], greater
    lst_parts = [lst[:]]
    while len(lst_parts) < len(lst):
        for i, e in enumerate(lst_parts):
            if len(e) > 1:
                l, p, g = partition(e)
                del lst_parts[i]
                if g:
                    lst_parts.insert(i, g)
                if p:
                    lst_parts.insert(i, p)
                if l:
                    lst_parts.insert(i, l)
            else:
                pass
    return [e[0] for e in lst_parts]


def quicksort(lst=[3, 7, 8, 5, 2, 1, 9, 5, 4]):
    if len(lst) > 1:
        less = []
        greater = []
        for i in lst[1:]:
            if i <= lst[0]:
                less.append(i)
            else:
                greater.append(i)
        return quicksort(less) + [lst[0]] + quicksort(greater)
    else:
        return lst


def main(lst):
    print(f'original list:{lst}',
          f'my version:{quicksort_(lst)}',
          f'pretty version:{quicksort(lst)}',
          sep='\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list',
                        nargs='+',
                        default=[3, 7, 8, 5, 2, 1, 9, 5, 4],
                        type=int)
    args = parser.parse_args()
    main(args.list)
