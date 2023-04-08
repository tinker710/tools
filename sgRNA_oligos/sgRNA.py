# -*- coding: utf-8 -*-
"""
author： lee
date: 2023-04-08
"""

import argparse
import os

def antisense(sense_seq):
    dict_ATGC = {"A":"T","T":"A","G":"C","C":"G"}
    antisense_seq = ""
    for i in sense_seq[-1::-1]:
        antisense_seq += dict_ATGC[i]
        #print(antisense_seq)
    return antisense_seq


parser = argparse.ArgumentParser(description="test")
parser.add_argument('--target', type = str)
parser.add_argument('--output', type = str)
args = parser.parse_args()

file_out = open(os.path.join(args.output,'oligos_out.txt'),"w")

with open(args.target, 'r') as file1:
    data1 = file1.readlines()
    for line in data1[1:]:
        name, target_seq = line.strip().split("\t")
        sense_seq = target_seq.upper()
        if sense_seq[0] != "G":
            sense_seq = "G"+sense_seq
        antisense_seq = antisense(sense_seq)
        forward_oligo = "cacc"+sense_seq
        reverse_oligo = "aaac"+antisense_seq
        file_out.write("{}_OF\t{}\n".format(name, forward_oligo))
        file_out.write("{}_OR\t{}\n".format(name, reverse_oligo))
file_out.close()
print("OK")
