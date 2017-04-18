hydrophobic_proteins=[ "A", "I" ,"L", "M", "F", "W", "Y", "V"]
def my_function(DNA, residues=hydrophobic_proteins ):
    count =0
    length = len(DNA)
    for base in DNA:
        for residue in residues:
            if base.upper() == residue.upper():
                count+=1

    return (count*100/length)


assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("msrslllrfllfllllpplp", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

# assert statements for part two
assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65
