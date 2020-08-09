# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    letters = ["abcdefghijklmnopqrstuvwxyz"]
    i = 0
    for i in range(len(letters[0])):
        if letter == letters[0][i]:
            return letters[0][i+1]
        if letter == letters[0][-1]:
            return letters[0][0]
        
print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a
