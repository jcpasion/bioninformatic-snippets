from Bio import Entrez
from Bio import SeqIO
Entrez.email = "omi319@sbcglobal.net" #input your email here





genes= ["JQ867090, JQ011276, NM_001265803, NM_214399, JX469983, NM_001246828, JN573266, JX462670, JX469991"] #input your id's here, make sure to put commas



#this function will get you your shortest sequence in a list of genes of interest, in FASTA format

def shortest_fasta_seq(ids):

    handle = Entrez.efetch(db="nucleotide", id = ids, rettype = "fasta") #fetch the data on your genes
    records = list(SeqIO.parse (handle, "fasta")) #turn the data into a list


    shortest_seq = records[0]

    for gene in records:
        if len(gene.seq) <= len(shortest_seq.seq):
            shortest_seq = gene #find the gene with the shortest gene and save it in "shortest_seq"

    print (shortest_seq)
    print (shortest_seq.seq)


print (shortest_fasta_seq(genes))