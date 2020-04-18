#!/usr/bin/env python
import os
import shutil
import glob
from Bio import SeqIO
 
#Enter directory where all genome directories are located
rootdir = "/path/to/dir"
 
#Enter final destination of newly created, renamed fasta files
renamed_folder = '/path/to/renamed'
 
 
#enter total # genome so we can see how far along the script is
start = 1
total = 18874
 
#Rename the headers of '_genomic.fna' files in all subdirs of the root
for subdir, dirs, files, in os.walk(rootdir):
    for file in files:
        if file.endswith('_genomic.fna'):
            os.chdir(subdir)
 
            #get strain name
            file_name = file.split('_genomic.fna')[0]
            print (file_name)
 
            #Remove the 'GCA_' and '.1' from the string
            strain = file.split('_')[1]
            strain = strain.split('.')[0]
 
            #initialize renamed output file
            outfile= open(file_name + '_renamed.fna', 'w')
 
            #initialize loop for naming contigs
            i=1
 
            myfastalist=list(SeqIO.parse(file,'fasta'))
            for record in myfastalist:
                desc = record.description
                seq = record.seq
 
                outfile.write('>' + strain + '_' +str(i) + ' ' + desc + '\n' + str(seq)  + '\n')
                i += 1
 
            outfile.close()
 
            #chmod the new, renamed file
            renamed = glob.glob('*_renamed.fna')
            for file in renamed:
                os.chmod(file,0o777)
 
 
            #Move file to renamed_folder
            for file in renamed:
                source = ( subdir + '/' +  file)
                dest = (renamed_folder + '/' + file)
                shutil.move(source, dest)
 
            #Print the fraction % the script is done
            print (str(((start/total)*100)) + '% finished')
            start += 1
