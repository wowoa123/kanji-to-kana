# -*- coding: utf-8 -*-

import sys
import MeCab

def lang_strucr_analy(sentence):
    mecab = MeCab.Tagger("-Oyomi")
    print(mecab.parse(sentence))
