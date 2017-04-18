

def BP_content(DNA):
   #make empty lists, get length of DNA, turn DNA string into list
    countAT = 0
    countGC =0
    len_DNA = len(DNA)
    listed_DNA = list(DNA)

    #adds 1 to correct count list
    for letter in listed_DNA:
        if letter.upper() =="A" or letter.upper() =="T":
            countAT+=1
        elif letter.upper() =="G" or letter.upper() == "C":
            countGC+=1
        else:
            continue

    #prints percentage of AT and GC
    print("AT Content:\n" + str(countAT/len_DNA))
    print("GC Content:\n" +str(countGC/len_DNA))
