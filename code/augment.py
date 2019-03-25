# @Author : zhany
# @Time : 2019/03/20 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eda import *

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="原始数据的输入文件目录")
ap.add_argument("--output", required=False, type=str, help="增强数据后的输出文件目录")
ap.add_argument("--num_aug", required=False, type=int, help="每条原始语句增强的语句数")
ap.add_argument("--alpha", required=False, type=float, help="每条语句中将会被改变的单词数占比")
args = ap.parse_args()

#输出文件
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#每条原始语句增强的语句数
num_aug = 9 #default
if args.num_aug:
    num_aug = args.num_aug

#每条语句中将会被改变的单词数占比
alpha = 0.1 #default
if args.alpha:
    alpha = args.alpha

def gen_eda(train_orig, output_file, alpha, num_aug=9):

    writer = open(output_file, 'w')
    lines = open(train_orig, 'r').readlines()

    print("正在使用EDA生成增强语句...")
    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')    #使用[:-1]是把\n去掉了
        label = parts[0]
        sentence = parts[1]
        aug_sentences = eda(sentence, alpha_sr=alpha, alpha_ri=alpha, alpha_rs=alpha, p_rd=alpha, num_aug=num_aug)
        for aug_sentence in aug_sentences:
            writer.write(label + "\t" + aug_sentence + '\n')

    writer.close()
    print("已生成增强语句!")
    print(output_file)

if __name__ == "__main__":
    gen_eda(args.input, output, alpha=alpha, num_aug=num_aug)
