#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize hOP')
parser.add_argument('data', help='hOP data directory')
args = parser.parse_args()

print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
print("@prefix dct: <http://purl.org/dc/terms/> .")
print('@prefix obo: <http://purl.obolibrary.org/obo/>')
print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print('@prefix probe: <http://identifiers.org/affy.probeset/>')
print()

# def print_profile(group_no, label, prifoke, member):
#     print(f'group:{group_no} a orth:OrthologsCluster ;')
#     print(f'    orth:inDataset <https://orth.dbcls.jp/data/hop/> ;')

# def print_profile(tissues):
#     for tissue in tissues:
#         print(' refexo:overExpressedIn ')
#         print(' '.join(tissues))

fp = open(args.data, 'r')
read_header = False
for line in fp:
    fields = line.strip().split('\t')
    probe = fields[0]
    if not read_header:
        read_header = True
        continue
    for i in range(2, len(fields)):
        val = fields[i]
        tissue_no = f'refexo:v{i-1}_40'
        if val == '1':
            print(f'probe:{probe} refexo:overExpressedIn ' + tissue_no + ' .')
        elif val == '-1':
            print(f'probe:{probe} refexo:underExpressedIn ' + tissue_no + ' .')
