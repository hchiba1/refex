#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx')
parser.add_argument('data', help='hOP data directory')
args = parser.parse_args()

print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print('@prefix affy: <http://identifiers.org/affy.probeset/>')
print('@prefix refseq: <http://identifiers.org/refseq/>')
print()

# def print_profile(group_no, label, prifoke, member):
#     print(f'group:{group_no} a orth:OrthologsCluster ;')
#     print(f'    orth:inDataset <https://orth.dbcls.jp/data/hop/> ;')

# def print_profile(tissues):
#     for tissue in tissues:
#         print(' refexo:overExpressedIn ')
#         print(' '.join(tissues))

fp = open(args.data, 'r')
checked_header = False
col_name = ''
prefix_name = ''
for line in fp:
    fields = line.strip().split('\t')
    col_name = fields[0]
    if not checked_header:
        checked_header = True
        if col_name == 'Affymetrix_probesetID':
            prefix_name = 'affy'
        elif col_name == 'NCBI_RefSeqID':
            prefix_name = 'refseq'
        continue
    for i in range(2, len(fields)):
        val = fields[i]
        if val == '1':
            print(f'{prefix_name}:{col_name} refexo:overExpressedIn refexo:v{i-1}_40 .')
        elif val == '-1':
            print(f'{prefix_name}:{col_name} refexo:underExpressedIn refexo:v{i-1}_40 .')
