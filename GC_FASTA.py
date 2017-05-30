from Bio import SeqIO
from Bio import Seq
from Bio.SeqUtils import GC

#this program will take in a fasta file with multiple genes, and print out the gene with the largest GC content

id=""
GC_content=0 #these will hold the gene with the largest GC content


for seq_record in SeqIO.parse("", "fasta"): #input your file name here, 
    seq = seq_record.seq #gives the sequence

    seq_id = seq_record.id #gives the id

    G_C = GC(seq) #compute GC content

    if G_C > GC_content: #changes id and GC_content if larger
        GC_content =G_C
        id = seq_id

print(id)
print (GC_content)
