#!/bin/bash

if (($# != 4)); then
    echo "Usage: $0 total group1 group2 overlap"
    echo "output P-less_enriched P-more_enriched"
    exit 1
fi

total=$1
group1=$2
group2=$3
overlap=$4

less_enriched=$(Rscript --vanilla -e "phyper($overlap, $group1, $total - $group1, $group2, lower.tail=T)" | sed -e 's/^\[1\] //')
more_enriched=$(Rscript --vanilla -e "phyper($overlap - 1, $group1, $total - $group1, $group2, lower.tail=F)" | sed -e 's/^\[1\] //')
echo $less_enriched $more_enriched
