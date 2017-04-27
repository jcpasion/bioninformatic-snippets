#this file gives the complement DNA strand
f = open("rosalind_revc.txt", "r")

#Convert into a list
DNA= f.read()
listed_DNA =list(DNA)

#empty list to append BP's
complement = []

#Remove spaces in the DNA just in case
if "\n" in listed_DNA:
    listed_DNA.remove('\n')

#Appends the complement BP
for letter in listed_DNA:
    if letter == "T":
        complement.append("A")
    elif letter == "A":
        complement.append("T")
    elif letter == "G":
        complement.append("C")
    elif letter == "C":
        complement.append("G")

#Joins the list into a string with no spaces, reverses it, and prints it
print (''.join(complement)[::-1])

