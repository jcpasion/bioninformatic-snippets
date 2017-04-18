import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def RandomMotifs(Dna, k, t):
    random_motifs = []
    for string in Dna:
        rand = random.randint(1, t - k)
        random_motifs.append(string[rand:rand + k - 1])

    return (random_motifs)




def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}  # output variable
    counts = CountWithPseudocounts(Motifs)
    for i in counts:
        for j in range(k):
            counts[i][j] = counts[i][j] / (t + 4)
    profile = counts
    return profile



def CountWithPseudocounts(Motifs):
    count = {}  # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def HammingDistance(string1, string2):
    list1 = list(string1)
    list2 = list(string2)

    Hamming = 0
    iter = 0
    for item in list1:
        if item.upper() != list2[iter].upper():
            Hamming += 1
        iter += 1
    return (Hamming)


def Score(Motifs):
    consensus = Consensus(Motifs)
    score = 0
    for motif in Motifs:
        x = HammingDistance(motif, consensus)
        score = score + x
    return (score)


def ProfileMostProbablePattern(Text, k, Profile):
    p = -1
    probable = ""
    for i in range(len(Text) - k + 1):
        current_prob = Pr(Text[i:i + k], Profile)
        if p < current_prob:
            probable = Text[i:i + k]
            p = current_prob
    return (probable)


def Pr(Text, Profile):
    p = 1
    k = len(Text)
    for i in range(k):
        p = p * Profile[Text[i]][i]
    return (p)
