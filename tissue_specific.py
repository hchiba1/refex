#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx tissue specificity data')
parser.add_argument('input_file', help='RefEx tissue specificity data file')
args = parser.parse_args()

fp = open(args.input_file, 'r')
checked_header = False
prefix = ''
for line in fp:
    fields = line.strip().split('\t')
    
    if not checked_header:
        checked_header = True
        print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
        if fields[0] == 'Affymetrix_probesetID':
            prefix = 'affy'
            print('@prefix affy: <http://identifiers.org/affy.probeset/>')
        elif fields[0] == 'NCBI_RefSeqID':
            prefix = 'refseq'
            print('@prefix refseq: <http://identifiers.org/refseq/>')
        print()
        continue
    
    for i in range(2, len(fields)):
        name = fields[0]
        val = fields[i]
        uri = f'{prefix}:{name}'
        if prefix == 'affy' and '/' in name:
            uri = f'<http://identifiers.org/affy.probeset/{name}>';
        if val == '1':
            print(f'{uri} refexo:isPositivelySpecificTo refexo:v{i-1}_40 .')
        elif val == '-1':
            print(f'{uri} refexo:isNegativelySpecificTo refexo:v{i-1}_40 .')
