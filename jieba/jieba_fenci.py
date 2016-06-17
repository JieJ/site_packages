# -*- coding: utf-8 -*-
"""
test jieba using user imported dictionary
"""

from datetime import datetime
import os
import sys
import jieba
import jieba.posseg as pseg

jieba.load_userdict("userdict.txt")

def jieba_cut(fname,fenci_fname):
    f = open(fenci_fname,'w')
    with open(fname) as xs:
        for l in xs.readlines():
            l = l.strip()
            res = pseg.cut(l)
            word_list = [word for word, flag in res]
            word_str = ' '.join(word_list)
            f.write(word_str.encode('utf8')+'\n')
    f.close()

def jieba_pseg(fname,fenci_fname, pos_fname, tag_fname):
    f1 = open(fenci_fname,'w')
    f2 = open(pos_fname,'w')
    f3 = open(tag_fname, 'w')
    with open(fname) as xs:
        for l in xs.readlines():
            l = l.strip()
            res = pseg.cut(l)
            token_list = []
            pos_list = []
            tag_list = []
            for token, pos in res:
                token_list.append(token)
                pos_list.append(pos)
                tag = token + '/' + pos
                tag_list.append(tag)
            token_str = ' '.join(token_list)
            pos_str = ' '.join(pos_list)
            tag_str = ' '.join(tag_list)
            f1.write(token_str.encode('utf8') + '\n')
            f2.write(pos_str.encode('utf8') + '\n')
            f3.write(tag_str.encode('utf8') + '\n')
    f1.close()
    f2.close()
    f3.close()

if __name__ == '__main__':
    start = datetime.now()

    input_dir = u'D:\\情感信息分类\\Machine-learning based Sentiment Classification Method\\coae2014'
    raw_fname = input_dir+os.sep+'neg'
    fenci_fname = input_dir+os.sep+'neg_fenci'
    jieba_cut(raw_fname,fenci_fname)


    input_dir = 'train'
    raw_fname = input_dir+os.sep+'pos_filted'
    fenci_fname = input_dir+os.sep+'pos_fenci'
    jieba_cut(raw_fname,fenci_fname)


    raw_fname = input_dir+os.sep+'neg_filted'
    fenci_fname = input_dir+os.sep+'neg_fenci'
    jieba_cut(raw_fname,fenci_fname)

    end = datetime.now()
    print end-start
    print 'over'
