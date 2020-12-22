#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx tissue specificity data')
parser.add_argument('input_file', help='RefEx tissue specificity data file')
args = parser.parse_args()

print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print('@prefix affy: <http://identifiers.org/affy.probeset/>')
print('@prefix refseq: <http://identifiers.org/refseq/>')
print()

fp = open(args.input_file, 'r')
checked_header = False
prefix = ''
for line in fp:
    fields = line.strip().split('\t')
    
    if not checked_header:
        checked_header = True
        if fields[0] == 'Affymetrix_probesetID':
            prefix = 'affy'
        elif fields[0] == 'NCBI_RefSeqID':
            prefix = 'refseq'
        continue
    
    for i in range(2, len(fields)):
        key = fields[0]
        val = fields[i]
        if val == '1':
            print(f'{prefix}:{key} refexo:overExpressedIn refexo:v{i-1}_40 .')
        elif val == '-1':
            print(f'{prefix}:{key} refexo:underExpressedIn refexo:v{i-1}_40 .')
