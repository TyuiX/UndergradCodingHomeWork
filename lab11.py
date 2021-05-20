# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Lab Assignment 11


def compress_dna_sequence(sequence, rules):
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    x = ''
    y = ''
    for i in sequence:
        x += comp[i]
    for i in range(0, len(x), 4):
        y += rules[x[i:i+4]]


    return y