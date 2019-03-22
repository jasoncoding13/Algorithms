# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:20:26 2019

@author: Jason
@e-mail: jasoncoding13@gmail.com
"""

import pandas as pd


def csv2dict():
    df = pd.read_csv('./data_stable_marriage.csv', index_col=0)
    dict_ = {}
    for g in ['M', 'F']:
        dict_[g] = {}
        for i in df.loc[df['Gender'] == g, :].index:
            dict_[g][i] = {}
            dict_[g][i]['perference'] = df.loc[i, :][2:].values.tolist() + [0]
            dict_[g][i]['capacity'] = df.loc[i, 'Capacity']
    return dict_


def find_matching(dict_, opt='M'):
    non_opt = ['M', 'F']
    non_opt.remove(opt)
    non_opt = non_opt[0]
    proposers = {k: 0 for k in dict_[opt].keys()}
    targets = {k: 0 for k in dict_[non_opt].keys()}
    while 0 in proposers.values():
        proposer = [k for k, v in proposers.items() if v == 0][0]
        for target in dict_[opt][proposer]['perference']:
            per = dict_[non_opt][target]['perference']
            proposer_ = targets[target]
            if (per.index(proposer) < per.index(proposer_)):
                proposers[proposer] = target
                targets[target] = proposer
                if proposer_:
                    proposers[proposer_] = 0
                    print(f'{proposer_} is denied by {target}.')
                else:
                    print(f'{target} is free.')
                print(f'So {proposer} is accepted by {target}.')
                break
            else:
                print(f'{proposer} is denied by {target}.')
    return proposers, targets


if __name__ == '__main__':
    dict_ = csv2dict()
    opts = ['M', 'F']
    for opt in opts:
        print(f'{opt}-optimal solution is',
              find_matching(dict_=dict_, opt=opt))
