#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx ID Relation')
parser.add_argument('input_file', help='RefEx ID Relation file')
args = parser.parse_args()

print('@prefix ncbigene: <http://identifiers.org/ncbigene/>')
print('@prefix ensg: <http://identifiers.org/ensembl/>')
print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print()

ensg_ncbigene = {}
ncbigene_ensg = {}

fp = open(args.input_file, 'r')
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) > 2:
        ensg_id = fields[0]
        ncbigene_id = fields[2]
        if ensg_id and ncbigene_id:
            ncbigene_ensg[f'{ncbigene_id}:{ensg_id}'] = True
            ensg_ncbigene[f'{ensg_id}:{ncbigene_id}'] = True

for key in sorted(ncbigene_ensg.keys()):
    [ncbigene_id, ensg_id] = key.split(':')
    print(f'ncbigene:{ncbigene_id} refexo:ensembl ensg:{ensg_id} .')

print()

for key in sorted(ensg_ncbigene.keys()):
    [ensg_id, ncbigene_id] = key.split(':')
    print(f'ensg:{ensg_id} refexo:ncbigene ncbigene:{ncbigene_id} .')
