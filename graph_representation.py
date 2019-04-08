# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:50:50 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

edges = [(1, 2),
         (1, 3),
         (2, 3),
         (2, 4),
         (2, 5),
         (3, 5),
         (3, 7),
         (3, 8),
         (5, 6)]


def edges2adjacency_list(edges):
    adjacency_list, len_ = [], 0
    for i, j in edges:
        max_ = max(i, j)
        if max_ > len_:
            for l in range(len_, max_):
                adjacency_list.append([])
            len_ = max_
        adjacency_list[i-1].append(j)
        adjacency_list[j-1].append(i)
    return adjacency_list


def edges2adjacency_matrix(edges):
    adjacency_matrix, len_ = [], 0
    for i, j in edges:
        max_ = max(i, j)
        if max_ > len_:
            for l in range(len_):
                adjacency_matrix[l] += [0]*(max_-len_)
            for l in range(len_, max_):
                adjacency_matrix.append([0]*max_)
            len_ = max_
        adjacency_matrix[i-1][j-1] = 1
        adjacency_matrix[j-1][i-1] = 1
    return adjacency_matrix
