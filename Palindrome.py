def reverse(s):
    rev= ""
    for ch in s:
        rev = ch+rev
    return (rev)

def is_palindrome1(s):
    rev = reverse(s)
    return rev == s

