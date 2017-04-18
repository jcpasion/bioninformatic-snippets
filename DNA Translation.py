import re
genetic_code = open("genetic_code.txt").read().strip("\n")
DNA = "ATGTATGTA"

# list of codons from the given DNA string
codons = []

# Translates the DNA string into a list of codons
def translate_dna(DNA):
    proteins = ""

    for start in range (0,len(DNA),3):
       codon = DNA[start:start+3]
       aa= genetic_code.get(codon,"X")
       proteins += proteins + aa

    print(proteins)
# translates the codons into a list of proteins, conectates them into a string



translate_dna(DNA)

