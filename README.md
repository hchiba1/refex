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

### Example SPARQL

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
