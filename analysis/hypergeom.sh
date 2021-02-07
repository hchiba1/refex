#!/bin/bash

if (($# != 4)); then
    echo "Usaga: $0 total sample1 sample2 overlap"
    exit 1
fi

total=$1
group1=$2
group2=$3
overlap=$4

less_enriched=$(Rscript --vanilla -e "phyper($overlap, $group1, $total - $group1, $group2)" | sed -e 's/^\[1\] //')
more_enriched=$(Rscript --vanilla -e "phyper($overlap - 1, $group1, $total - $group1, $group2, lower.tail=F)" | sed -e 's/^\[1\] //')
echo $less_enriched $more_enriched
