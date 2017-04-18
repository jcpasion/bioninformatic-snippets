import itertools

list = (list(itertools.permutations((1,2,3,4,5), r=5)))

print (len(list))
print(list)

for perm in list:
    perm.strip(",")