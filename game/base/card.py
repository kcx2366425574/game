#!/usr/bin/env python
# encoding: utf-8
'''
@author: kuangcx
@contact: kuangcx@inspur.com
@software: pycharm
@file: card.py
@time: 2021/4/17 1:09 下午
@desc: 
'''
import itertools
import random

PUKE_CARD_TYPE = 4
PUKE_CARD_TYPE_VALUE = ["♥️", "♦️", "♠️", "♣️"]
PUKE_CARD_VALUE_13 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
PUKE_CARD_VALUE_15 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "小王", "大王"]

PUKE_CARD_VALUE_SIZE = {
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    "2": 15,
    "小王": 16,
    "大王": 17
}


class card:

    def __init__(self, type_count, card_type, card_type_value, card_value=None):

        # 牌的数字种类数 int
        self.type_count = type_count

        # 牌的花色种类数 int
        self.card_type = card_type

        # 牌的各个花色值[]
        self.card_type_value = card_type_value

        # 牌的数字值[]
        self.card_value = card_value if card_value else [i + 1 for i in range(len(type_count))]


class puke(card):

    def __init__(self, pair_number=1, type_count=13):
        # 几副牌
        self.pair_number = pair_number

        # 一共多少张牌
        self.total_nums = self.pair_number * type_count * len(PUKE_CARD_TYPE_VALUE)

        if type_count == 13:
            card_value = PUKE_CARD_VALUE_13
        elif type_count == 15:
            card_value = PUKE_CARD_VALUE_15
        else:
            raise NotImplementedError
        super().__init__(type_count, PUKE_CARD_TYPE, PUKE_CARD_TYPE_VALUE, card_value)

        # 一共有哪些牌
        self.card_list = ["".join(result) for result in itertools.product(self.card_type_value, self.card_value)]
