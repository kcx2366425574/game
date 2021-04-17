#!/usr/bin/env python
# encoding: utf-8
'''
@author: kuangcx
@contact: kuangcx@inspur.com
@software: pycharm
@file: api.py
@time: 2021/4/17 4:54 下午
@desc: 
'''
from game.base.card import puke
from game.utils.puke_util import get_puke

if __name__ == '__main__':
    players = 4
    puke_instance = puke()
    card_list = get_puke(players, puke_instance, sort="number")
    for card in card_list:
        print(card)
