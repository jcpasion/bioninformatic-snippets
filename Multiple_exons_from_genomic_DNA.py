DNA = open("genomic_dna.txt")
exon = open("exons.txt")
list_DNA = DNA.read()




con_DNA = []
for line in exon:
    #split line by the ,
    split_line = str(line).split(",")

    #strip the \n
    strip_line =[split_line[0], split_line[1].rstrip("\n")]

    #turn list objects into integers
    start= int(strip_line[0])
    stop = int(strip_line[1])

    #appends the exon to a list
    exon_DNA = list_DNA [start:stop]
    con_DNA.append(exon_DNA)

#join the list together with no space between
joined_exon =''.join(con_DNA)


#write to the output file and close
concatenated_DNA = open("concatenated_DNA.txt", "w")
concatenated_DNA.write(joined_exon)
concatenated_DNA.close()