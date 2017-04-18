def mendel_1st (homoD,hetero, homoR):
    #there are "sum" amount of alleles in this population
    total = (homoD + hetero + homoR)*2

    #count the number of each allele in the population
    DH= (homoD*2 + hetero)
    RR= (homoR*2 + hetero)

    # calculate probabilities of offspring being homoD, homoR, or hetero
    probD = (DH)/total * (DH-1)/(total -1)
    probR =(RR)/total * (RR-1)/(total -1)
    probhetero = ((DH)/total * (RR)/(total -1))+ ((RR)/total * (DH)/(total -1))

    #Add's prob of being DH and prob of being HZ
    return("Probability of expressing Dominant Allele: " + str(probD+ probhetero))

