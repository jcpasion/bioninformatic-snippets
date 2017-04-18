# finds the length of the substrings after a cut in the DNA

def substring_length(DNA,recog_site):
    Cut = DNA.find(recog_site)
    Substring1 = len(DNA[0:Cut])
    Substring2 = len(DNA [Cut:])

    print (Substring1)
    print (Substring2)

substring_length("TACTACTACTACTACTACTACTACTACTACTG", "ACT")