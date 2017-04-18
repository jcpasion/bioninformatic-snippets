f = open("rosalind_rna.txt", "r")

# turn the DNA into a list and remove "\n"
listed = list(f.read())
listed.remove("\n")

#The for-loop iterates on the string and appends it to transcribed
# If it sees a T, it appends U, otherwise appends the object
transcribed = []
if "\n" in listed:
    listed.remove('\n')
for letter in listed:
    if letter == "T":
        transcribed.append("U")
    else:
        transcribed.append(letter)

#joins the list together into a single string with no spaces
print (''.join(transcribed))
