# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:13:55 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

from collections import defaultdict

edges = [(1, 2),
         (1, 3),
         (2, 3),
         (2, 4),
         (2, 5),
         (3, 5),
         (3, 7),
         (3, 8),
         (5, 6)]


def edges2dict_graph(edges, directed=False):
    dict_graph = defaultdict(list)
    for i, j in edges:
        dict_graph[i].append(j)
        if not directed:
            dict_graph[j].append(i)
    return dict(dict_graph)


def breath_first_search_(dict_graph, s=None):
    if not s:
        s = list(dict_graph.keys())[0]
    edges_bfs_tree = []
    nodes_searched = [s]
    current_layer = [s]
    while current_layer:
        next_layer = []
        for node in current_layer:
            for neighbour in dict_graph[node]:
                if neighbour not in nodes_searched:
                    nodes_searched.append(neighbour)
                    next_layer.append(neighbour)
                    edges_bfs_tree.append((node, neighbour))
        current_layer = next_layer[:]
    bfs_tree = edges2dict_graph(edges_bfs_tree, directed=True)
    return bfs_tree


def breath_first_search(
        dict_graph, s=None, dist=False, ret_edges_searched=False):
    if not s:
        s = list(dict_graph.keys())[0]
    edges_bfs_tree = []
    dist = {s: 0}
    edges_searched = []
    nodes_searched = [s]
    queue_nodes = [s]
    while queue_nodes:
        node = queue_nodes.pop()
        for neighbour in dict_graph[node]:
            if neighbour not in nodes_searched:
                nodes_searched.append(neighbour)
                queue_nodes.append(neighbour)
                edges_bfs_tree.append((node, neighbour))
                dist[neighbour] = dist[node] + 1
                edges_searched.append((s, neighbour))
    bfs_tree = edges2dict_graph(edges_bfs_tree, directed=True)
    output = {'bfs_tree': bfs_tree}
    if dist:
        output['distance'] = dist
    if ret_edges_searched:
        output['edges_searched'] = edges_searched
    return output


def get_transitive_closure(dict_graph):
    dict_closure = {}
    for n in dict_graph.keys():
        output = breath_first_search(dict_graph, s=n, ret_edges_searched=True)
        dict_closure[n] = [v for k, v in output['edges_searched']]
    return dict_closure
