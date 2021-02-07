#!/usr/bin/env python3
import sys
from scipy.stats import hypergeom

if (len(sys.argv) != 5):
    print("Usage: ./hypergeom.py total sample1 sample2 overlap")
    sys.exit(1)

total = int(sys.argv[1])
group1 = int(sys.argv[2])
group2 = int(sys.argv[3])
overlap = int(sys.argv[4])

less_enriched = hypergeom.cdf(overlap, total, group1, group2)
more_enriched = hypergeom.sf(overlap - 1, total, group1, group2)
print(less_enriched, more_enriched)
