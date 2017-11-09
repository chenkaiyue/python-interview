#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import re

def cal_similar_words(word):
    if len(word) != 0: #空行排除掉
        for item in word:
            pattern = word.replace(item,'.')
            words_dict[pattern].add(word)

words_list=[]
words_dict = defaultdict(set)

#下面这种是针对文件不太大的
# with open(r"listing20-1.txt",'r') as f:
#     words_list = re.findall(r'\w+',f.read())

#对于文本比较多的，还是不要一次读入，最好是用readline
with open(r"listing20-1.txt",'r') as f:
# with open("D:/coding git/python-interview/大数据处理/listing20-1.txt",'r') as f:
    line = f.readline()
    while line:
        words_list += re.findall(r'\w+',line)
        line = f.readline()

for item in words_list:
    cal_similar_words(item)

for key,value in words_dict.items():
    lenv = len(words_dict[key])
    if lenv >= 2:
        print "key: %s" % key
        # print words_dict[key]
        print value
        print ""