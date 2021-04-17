#!/usr/bin/env python
# encoding: utf-8
'''
@author: kuangcx
@contact: kuangcx@inspur.com
@software: pycharm
@file: puke_util.py
@time: 2021/4/17 4:56 下午
@desc: 
'''
import random

from game.base.card import PUKE_CARD_VALUE_SIZE


def get_puke(players, card, sort="number"):
    total_card = card.card_list
    count = card.total_nums//players
    card_list = [[0 for col in range(count)] for row in range(players)]
    for i in range(players):
        for j in range(count):
            index = random.randint(0, len(total_card)-1)
            card_list[i][j] = total_card.pop(index)

        if sort in ["number"]:
            card_list[i].sort(key=lambda x: PUKE_CARD_VALUE_SIZE.get(x[2:]))
        elif sort in ["type"]:
            card_list[i].sort(key=lambda x: x[0])

    return card_list
