#!/usr/bin/env python3
import os
import sys
import gzip
from Bio import SeqIO

#functions for trimming and merging fastq files, and characterizing fastq files

def cut_primers(file, primer, raw_dir, trimmed_dir):
    #Cut primer sequences off from beginning of a read and send to new "trimmed" file
    #Input: zipped fastq file
    #Output: new fastq.gz file with primers trimmed off
    
    print(file)
    with gzip.open(file, "rt") as handle:
        fq_record = (SeqIO.parse(handle, 'fastq'))

        #Add a record to trimmed file if sequence starts with primer, then cut the primer sequence off 
        trimmed_primer_reads = (rec[8:] for rec in fq_record if rec.seq.startswith(primer))
        
        trimmed_file_name = file.replace(".fastq.gz","_trimmed.fastq").replace(raw_dir, trimmed_dir) 
        count = SeqIO.write(trimmed_primer_reads, trimmed_file_name, "fastq")
       

###

def merge_reads(file1, file2, trimmed_dir, merged_dir, orphan_dir):
    #Create interleaved merged fastq and orphaned reads fastq files
    #Input: paired end fastq files, and directories for trimmed, and output dirs
    #output: print statements, merged fastq, orphan fastq

    #import indexes for fq_1 and fq_2
    fq_dict_1 = SeqIO.index(trimmed_dir + "/" + file1,"fastq")
    fq_dict_2 = SeqIO.index(trimmed_dir + "/" + file2,"fastq")
    
    #find all reads that are present in both, and find orphan reads
    
    orphan_reads_1 = []
    orphan_reads_2 = []
    both_fq= []

    for key in fq_dict_1.keys():
        if key in fq_dict_2.keys():
            both_fq.append(key)
        else:
            orphan_reads_1.append(key)
    
    for key in fq_dict_2.keys():
        if key not in both_fq:
            orphan_reads_2.append(key)

    #Create filename for the merged and orphan fastq file 
    output_merge = (file1.replace("_1_trimmed.fastq","_trimmed_merged.fastq"))
    output_orphan = (file1.replace("_1_trimmed.fastq","_trimmed_orphans.fastq"))
    
    #Print statements for summaries
    print (output_merge)
    print("Total matched reads: " + str(len(both_fq)))

    print (output_orphan)
    print("Total orphan reads: "  + str(len(orphan_reads_1) + len(orphan_reads_2)))

    #initialize paired and orphan fastq files
    fh_merged = open(merged_dir + "/" + output_merge, "w")
    fh_orphan = open(orphan_dir + "/" + output_orphan,"w")

    #create the merged file where read 1 and read 2 are interleaved 
    for id in both_fq:
        read_1 = (fq_dict_1.get_raw(id).decode())
        read_2 = (fq_dict_2.get_raw(id).decode())
        fh_merged.write(read_1)
        fh_merged.write(read_2)
    
    #create the orphaned file where reads didn't have matches
    for id in orphan_reads_1:
        read = (fq_dict_1.get_raw(id).decode())
        fh_orphan.write(read)

    for id in orphan_reads_2:
        read_2 = (fq_dict_2.get_raw(id).decode())
        fh_orphan.write(read)

    fh_merged.close()
    fh_orphan.close()    

###

def characterize_final_fastq(file, merged_dir, orphan_dir):
    #Get summary stats for final merged fastqc files
    #Input: unzipped fastq file, directory of unzipped fastq file, directory of orphan file
    #Output: tsv format of summary stats for this file

    #initialize counts and lists
    record_count = 0
    read_lengths = []
    bad_qc_reads = 0
    orphan_count = 0
    
    #open final merged fastq
    fh=open(merged_dir + "/" + file)
    fq_record = (SeqIO.parse(fh, 'fastq'))

    #add record to record count and len to read lengths
    for record in fq_record:
        record_count += 1
        read_lengths.append(len(record.seq))

        #If records average phred score is less than 20, note it
        if sum(record.letter_annotations["phred_quality"])/len(record.letter_annotations["phred_quality"]) < 20:
            bad_qc_reads += 1 

    #Get the file name for the orphaned read fastq
    orphan_file_name = file.replace("_merged", "_orphans")

    #Open the orphan read fastqs
    fh_orphan = open (orphan_dir + "/" + orphan_file_name)
    fq_record_orphan = (SeqIO.parse(fh_orphan, "fastq"))
    
    #Add orphan counts to orphan_count
    for record in fq_record_orphan:
        orphan_count += 1

    #Summary stats of read lengths
    avg = (sum(read_lengths)/len(read_lengths))
    minimum = min(read_lengths)
    maximum = max(read_lengths)
    
    #return record count, bad qc reads, orphan #, avg read length, min read length, max read length
    return (str(record_count) + "	" + str(bad_qc_reads) + "	" + str(orphan_count) + "	" + str(avg) + "	" + str(minimum) + "	" + str(maximum))


