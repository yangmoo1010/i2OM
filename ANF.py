#!/usr/bin/env python
# _*_coding:utf-8_*_

import sys, os
import csv

def ANF(fastas):

    ANFdata = open(f"./fasta_cache/{fastas}", "r").readlines()

    encodings = []
    header = []
    for l in range(1, 42):
        header.append('ANF_' + str(l))
    encodings.append(header)
    
    for i in ANFdata:
        if i[0] != '>':
            code = []
            sequence = i
            for j in range(len(sequence.strip())):
                code.append(sequence[0: j + 1].count(sequence[j]) / (j + 1))
            encodings.append(code)
    with open(f"./feature_cache/{fastas[0]}_ANF.csv", "w", newline='') as d:
        writer = csv.writer(d)
        for r in encodings:
            writer.writerow(r)

    return 0

