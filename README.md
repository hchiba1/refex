# RefEx ver1 additional RDF

Database Center for Life Science

Attribution 4.0 International (CC BY 4.0)

https://creativecommons.org/licenses/by/4.0/

## Original data

https://refex.dbcls.jp/download.php

https://integbio.jp/rdf/dataset/refex

https://refex.dbcls.jp/about.php

https://github.com/dbcls/RefEx/tree/master/Rawdata_Processing

## Additionally created RDF

```
./tissue_specific.py original_data/RefEx_tissue_specific_genechip_human_GSE7307.tsv > created_rdf/RefEx_tissue_specific_genechip_human_GSE7307.ttl
```

```
./tissue_specific.py original_data/RefEx_tissue_specific_RNAseq_human_PRJEB2445.tsv > created_rdf/RefEx_tissue_specific_RNAseq_human_PRJEB2445.ttl 
```

```
./id_relation.py original_data/RefEx_ID_Relation_human.tsv > created_rdf/RefEx_ID_Relation_human.ttl
```

## Additonal cross-reference

How to get the additional cross-reference from BioMart

```
wget -O biomart_id_relation 'http://www.ensembl.org/biomart/martservice?query=<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "TSV" header = "0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Attribute name = "ensembl_gene_id" /><Attribute name = "ensembl_transcript_id" /><Attribute name = "entrezgene_id" /> <Attribute name = "hgnc_symbol" /><Attribute name = "affy_hg_u133_plus_2" /></Dataset></Query>'
```

## Example SPARQL

Test endpoint: 
https://orth.dbcls.jp/sparql-dev

```
PREFIX refexo: <http://purl.jp/bio/01/refexo#>

SELECT DISTINCT ?gene
WHERE {
  ?gene refexo:affyProbeset ?affy .
  ?affy refexo:isPositivelySpecificTo refexo:v32_40 .
}
```

## Statistical analysis

### Significance test using hypergeometric distribution

Using **R** `phyper()`
```
$ ./analysis/hypergeom.sh
Usage: ./analysis/hypergeom.sh total group1 group2 overlap
output P-less_enriched P-more_enriched
```
```
$ ./analysis/hypergeom.sh 19129 200 580 22
1 1.958805e-07
```
* total gene count: 19129
* liver-specific genes: 200
* conserved up to fungi: 580
* _P_[ overlap <= 22 ] = 1
* _P_[ overlap >= 22 ] = 1.958805e-07

Using **SciPy stats** `hypergeom.cdf()` or `hypergeom.sf()`
```
$ ./analysis/hypergeom.py 19129 200 580 22
0.999999954557 1.95880490138e-07
```
