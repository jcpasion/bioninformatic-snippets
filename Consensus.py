
#Given a list of equal length strings, these functions will find the IUPAC degenerate BP consensus strand

Strings = ["AACAGAG", "ACCAAAG", "AGCAGAG","ATCAAAG" ]

#ANCARAG is the expected consensus string


def consensus_base(string):
    string = string.upper()

    #conditional statements for all IUPAC degenerate pairs with A
    if "A" in string:

        if "T" in string:

            if "G" in string:

                if "C" in string:
                    return "N"
                else:
                    return "D"
            elif "C" in string:
                return "H"
            else:
                return "W"

        elif "G" in string:

            if "C" in string:
                return "V"
            else:
                return "R"
        elif "C" in string:
            return "M"
        else:
            return "A"


    #conditional statements for all IUPAC degenerate pairs with T, G and C
    elif "T" in string:

        if "G" in string:

            if "C" in string:
                return "B"

            else:
                return "K"
        elif "C" in string:
            return "Y"
        else:
            return "T"

    #conditional statements for all IUPAC degenerate pairs with G and C
    elif "G" in string:

        if "C" in string:
            return "S"
        else:
            return "G"


    elif "C" in string:
        return "C"

    else:
        print ("Sequence has unidentified letter")




def align (string_list):
    sequences= []
    len_string = len(string_list[0])
    Final_consensus = ""


    # turns the string_list into a list of lists, each Base is its own item within it's list
    for string in string_list:
        sequence = list(string)
        sequences.append(sequence)

    #add the ith index base from each list into a single string, and find the consensus on it, appending to Final_consensus
    for i in range(len_string):

        prelim = ""
        for sequence in sequences:
            prelim += sequence[i]

        base = consensus_base( prelim)
        Final_consensus+= base

    return (Final_consensus)



print (align(Strings))

