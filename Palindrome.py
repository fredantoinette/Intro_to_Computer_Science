###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# (no loops or conditions)

word = "madam"
# test case 2
word = "madman" # uncomment this to test

###

is_palindrome = word.find(word[::-1])

# TESTING
print(is_palindrome)
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"