#function returns the reverse of a string
def reverse(s):
    rev= ""
    for ch in s:
        rev = ch+rev
    return (rev)

#function determines if string is a palindrome
def is_palindrome1(s):
    rev = reverse(s)
    return rev == s

