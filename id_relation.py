#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='RDFize RefEx ID Relation')
parser.add_argument('input_file', help='RefEx ID Relation file')
args = parser.parse_args()

print('@prefix ncbigene: <http://identifiers.org/ncbigene/>')
print('@prefix refexo: <http://purl.jp/bio/01/refexo#>')
print('@prefix refseq: <http://identifiers.org/refseq/>')
print('@prefix affy: <http://identifiers.org/affy.probeset/>')
print()

fp = open(args.input_file, 'r')
checked_header = False
checked_relation = {}
for line in fp:
    if not checked_header:
        checked_header = True
        continue
    
    fields = line.strip().split('\t')
    gene_id = fields[0]
    refseq_id = fields[2]
    affy_id = fields[3]
    
    if refseq_id and (gene_id, refseq_id) not in checked_relation:
        print(f'ncbigene:{gene_id} refexo:refSeq refseq:{refseq_id} .')
        checked_relation[(gene_id, refseq_id)] = True
        
    if affy_id and (gene_id, affy_id) not in checked_relation:
        print(f'ncbigene:{gene_id} refexo:affyProbeSet affy:{affy_id} .')
        checked_relation[(gene_id, affy_id)] = True
