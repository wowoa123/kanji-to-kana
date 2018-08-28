# -*- coding: utf-8 -*-

import sys
import MeCab


class to_kana:
    def __init__(self, sentence):
        mecab = MeCab.Tagger("-Oyomi")
        print(mecab.parse(sentence))