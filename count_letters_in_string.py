# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


def palindrome(s):
    return s == s[:-1]

'''
number + letter

'''
def letter_count(s): # apple
    print(s)
    n = len(s) #5
    
    if n==0:
        return s
    
    if n==1:
        return "1" + s
    
    letters = s.strip('') # [a,p,p,l,e]
    print("letters", letters)
    result = {}
    result[letters[0]] = 1 # result[a] = 1
    
    char_count = ""
    for i in range(1, n):
        if letters[i] == letters[i-1]: # a!=p , p=p, l!=p, l!=e
            result[letters[i]] += 1 #result[p] = 2
        else:
            # append count to char
            char_count += str(result[letters[i-1]]) + (result[letters[i-1]] *letters[i-1]) # '1a2p1l'
            result[letters[i]] = 1 # result[e] = 1
        print("char_count is", char_count, " and result is", result)
    char_count += str(result[letters[i]]) + (letters[i])
    print ("out of for loop", char_count)
    return char_count
        
assert letter_count('apple') == '1a2pp1l1e'
assert letter_count('banana') == '1b1a1n1a1n1a'
assert letter_count('Mississippi') == '1M1i2ss1i2ss1i2pp1i'