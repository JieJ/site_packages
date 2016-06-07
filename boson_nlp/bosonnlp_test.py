# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:08:19 2015

@author: JieJ
"""

from bosonnlp import BosonNLP


if __name__ == '__main__':
    # # look up the usage condition
    # HEADERS = {'X-Token': 'RvfFdvC_.4154.f2IbbrWgZrP8'}
    # RATE_LIMIT_URL = 'http://api.bosonnlp.com/application/rate_limit_status.json'
    # import requests
    # result = requests.get(RATE_LIMIT_URL, headers=HEADERS).json()
    # for key,val in result['limits'].iteritems():
    #     print key,'\t',val

    nlp = BosonNLP('RvfFdvC_.4154.f2IbbrWgZrP8')
    nlp = BosonNLP('vQdBA8k_.4176.hUiXrb6354i2')    #LiYB's token
    nlp = BosonNLP('6pcRO9QY.4254.H0BK-v3mB5Cv')    #WangLY's token

    # s = ['对于该小孩是不是郑尚金的孩子，目前已做亲子鉴定，结果还没出来，'
    # '纪检部门仍在调查之中。成都商报记者 姚永忠']
    # result = nlp.ner(s)
    # print result
    # print ' '.join([x for x in result[0]['word']])

    fname = 'D:\\Github\\Sentiment-Analysis\\data\\nlpcc_emotion\\train\\neg_raw'
    all_texts = [x.strip() for x in open(fname).readlines()]
    for i in range(7000):
        print "handing "+str(i+1)+"th 100 documents....."
        start = i*100
        end = start+100
        if start >= len(all_texts):
            break
        texts = all_texts[start:end]
        # 连续空格只保留1个 繁体转化为简体 新词枚举强度设为3（较强）特殊字符不进行转化
        result = nlp.tag(texts, space_mode=1, oov_level=3, t2s=1, special_char_conv=0)
        f1 = open(fname + '_fenci', 'a')
        f2 = open(fname + '_pos', 'a')
        f3 = open(fname + '_cobine', 'a')
        for d in result:
            fenci_text = ' '.join([x.encode('utf8') for x in d['word']])
            pos_text = ' '.join(['tag_'+x.encode('utf8') for x in d['tag']])
            cobine_text = ' '.join([x.encode('utf8') + '/' + y.encode('utf8') for x, y in zip(d['word'], d['tag'])])
            f1.write(fenci_text + '\n')
            f2.write(pos_text + '\n')
            f3.write(cobine_text + '\n')
        f1.close()
        f2.close()
        f3.close()
    print 'over'
