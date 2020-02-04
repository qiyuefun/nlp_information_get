"""
    作者：郑发辉
    日期：2020.02.04
    版本：v1.0
    功能：问答系统
"""
import json
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter

# 防止中文乱码
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def QetQuestionAnswerInformation(input_path):
    """
    获取问答系统数据库内容
    :param input_path: 输入路径
    ：qlist  存储问题列表
    ：alist 存储答案列表
    :return: qlist alist
    """
    qlist= []
    alist= []
    data = json.load(open(input_path, encoding='utf-8'))
    data_list = data.get('data')
    for item in data_list:
        paragraphs = item.get("paragraphs")
        for paragraph in paragraphs:
            qas_list = paragraph.get('qas')
            for qas in qas_list:
                if not qas.get('is_impossible'):
                    qlist.append(qas.get("question"))
                    answer = qas.get("answers")[0]
                    alist.append(answer.get('text'))

    assert(len(qlist) == len(alist))
    return qlist, alist

def main():
    """

    :return:
    """
    qlist ,alist  = QetQuestionAnswerInformation('./train-v2.0.json')
    print('qlist,alist ：%d' % len(qlist))
    print(qlist[0])
    print(alist[0])
    print(qlist[1])
    print(alist[1])
if __name__ == '__main__':
    main()
