# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:20:26 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import pandas as pd


def csv2dict():
    df = pd.read_csv('./matrixes4stable_matching.csv', index_col=0)
    dict_ = {}
    for g in ['M', 'F']:
        dict_[g] = {}
        for i in df.loc[df['Gender'] == g, :].index:
            dict_[g][i] = {}
            dict_[g][i]['perference'] = df.loc[i, :][2:].values.tolist() + [0]
            dict_[g][i]['capacity'] = df.loc[i, 'Capacity']
    return dict_


def find_matching(dict_, opt='M'):
    proposers = list(dict_[opt].keys())
    non_opt = ['M', 'F']
    non_opt.remove(opt)
    non_opt = non_opt[0]
    match = {e: 0 for e in list(dict_[non_opt].keys())}
    while 0 in match.values():
        proposer = [p for p, t in zip(proposers, match.values()) if t == 0][0]
        for target in dict_[opt][proposer]['perference']:
            per = dict_[non_opt][target]['perference']
            partner = match[target]
            if (per.index(proposer) < per.index(partner)):
                match[target] = proposer
                if partner:
                    print(f'{target} denies {partner}.')
                else:
                    print(f'{target} is free.')
                print(f'{target} accepts {proposer}.')
                break
    return match


def swap_key_value(dict_):
    dict_ = {v: k for k, v in dict_.items()}
    return dict_


if __name__ == '__main__':
    dict_ = csv2dict()
    opts = ['M', 'F']
    for opt in opts:
        output = find_matching(dict_=dict_, opt=opt)
        output = swap_key_value(output) if opt == 'F' else output
        print(f'{opt}-optimal solution is', output)
