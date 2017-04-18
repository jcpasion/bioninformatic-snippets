import re
DNA = open("dna.txt",).read().strip("\n")

#creates a list for fragments to be appended to, starting with position 0
all_cut= [0]

#Cuts the DNA with ACG1 Restriction Enzyme, appends positions to all_cut
for match in re.finditer(r"A[ATCG]TAAT", DNA):
    all_cut.append(match.start()+3)

#Cuts the DNA with ACG2 Restriction Enzyme, appends positions to all_cut
for match in re.finditer(r"GC[AG][AT]TG",DNA):
    all_cut.append(match.start()+4)

#Adds the length of the DNA to all_cut and sorts out the list
all_cut.append(len(DNA))
sorted_cuts = sorted(all_cut)

#prints out the lengths of each fragment after digestion
for i in range(1,len(sorted_cuts)):
    current_position = sorted_cuts[i]
    previous_positon = sorted_cuts[i-1]
    print(current_position - previous_positon)