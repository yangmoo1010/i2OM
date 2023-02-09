#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys, os
import csv

def NCP(fastas):

    chemical_property = {
    'A': [1, 1, 1],
    'C': [0, 1, 0],
    'G': [1, 0, 0],
    'T': [0, 0, 1],
    'U': [0, 0, 1],
    'N': [0, 0, 0],
    }
    NCPdata = open(f"./fasta_cache/{fastas}", "r").readlines()
    encodings = []
    header = []
    for l in range(1, 41 * 3 + 1):
        header.append('NCP_'+str(l))
    encodings.append(header)

    for i in NCPdata:
        if i[0] != '>':
            sequence = i
            code = []
            for aa in sequence.strip():
                code = code + chemical_property.get(aa, [0, 0, 0])
                # print(len(code))
            encodings.append(code)
    with open(f"./feature_cache/{fastas[0]}_NCP.csv", "w", newline='') as d:
        writer = csv.writer(d)
        for r in encodings:
            writer.writerow(r)
    return 0

