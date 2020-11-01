#!/usr/bin/env python3
import os
import sys
import gzip
import csv
from fastq_functions import *
from Bio import SeqIO

#set rootdir where demultiplexed fastq.gz files are
raw_dir = ("/Users/julius/Desktop/Julius_coding_challenge/demultiplexed_fastqs")

#directories for each type of processed file
trimmed_dir = ("/Users/julius/Desktop/Julius_coding_challenge/trimmed_fastqs")
merged_dir = ("/Users/julius/Desktop/Julius_coding_challenge/merged_fastqs")
orphan_dir = ("/Users/julius/Desktop/Julius_coding_challenge/orphan_fastqs")

#Use the fastq_and_index.csv to trim the primers off of each fastq.gz file, only keeping reads that start with the primer sequence
with open("/Users/julius/Desktop/julius_coding_challenge/metadata/fastq_and_index.csv", newline="") as csvfile:
    for line in csvfile:
        line = line.strip("\n").strip("\r")
        data = line.split(",")
    
        cut_primers(raw_dir+ "/" + data[0],
                    data[1],raw_dir,trimmed_dir)


#Use the merge_pairs metadata to merge files and create orphans read files
with open("/Users/julius/Desktop/Julius_coding_challenge/metadata/merge_pairs.csv", newline="") as csvfile:
    for line in csvfile:
        line = line.strip("\n").strip("\r")
        data = line.split(",")
    
        merge_reads(data[0],
                    data[1],
                    trimmed_dir,
                    merged_dir,
                    orphan_dir)


# Open summary_stats tsv file and add headers
tsv_final = open("final_summary_stats.tsv","w+")
tsv_final.write("Sample Name" + "	" + "# Total Reads" + "	" "# Bad QC Reads" + "	" + "# Orphan Reads" + " 	" + "Average Read Length" + "	" + "Min Read Length" + "	" + "Max Read Length" + "\n")

#Generate summary stats for each of the final, merged fastq samples
for subdir,dirs,files, in os.walk (merged_dir):
    for file in files:
        if file.endswith(".fastq"):
            print(file)
        path_to_file = os.path.join(subdir, file)

        characterize = characterize_final_fastq(file, merged_dir, orphan_dir)

        tsv_final.write(file + "	" + characterize + "\n")

tsv_final.close()
