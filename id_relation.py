#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx ID Relation')
parser.add_argument('data', help='RDFize RefEx ID Relation')
args = parser.parse_args()

print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print('@prefix ncbigene: <http://identifiers.org/ncbigene/>')
print('@prefix affy: <http://identifiers.org/affy.probeset/>')
print()

fp = open(args.data, 'r')
read_header = False
for line in fp:
    fields = line.strip().split('\t')
    if not read_header:
        read_header = True
        continue
    gene = fields[0]
    refseq = fields[2]
    affy = fields[3]
    if affy:
        print(f'ncbigene:{gene} refexo:affyProbeSet affy:{affy}')
