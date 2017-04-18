f = open('rosalind_dna (2).txt', 'r')
g = f.read()

h = list(g)
h.remove("\n")
def word_count(text):
    words = {}
    for word in text:
        if word in words:
            words[word]+=1
        else:
            words[word] = 1
    return (words)



print(word_count(h))

f.close()