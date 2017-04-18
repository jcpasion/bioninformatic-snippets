#this program prints out the even numbers of a poem
f = open('rosalind_ini5.txt', 'r')

#convert poem into a list of lines
g= f.readlines()

#get only the even numbered lines
h =g[1::2]

#prints the lines
for line in h:
    print (line)






