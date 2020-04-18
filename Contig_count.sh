#!/bin/bash
 
#Count Contigs in a directory full of fasta files

dir=$(echo path/to/dir)
strains=$(ls ${dir})
 
echo "Strain, Contig_count" > contig_counts.csv

for i in $strains ; do
    count=$(grep '>' ${dir}/$i/${i}_genomic.fna | wc -l)
    echo "$i,$count" >> contig_counts.csv
