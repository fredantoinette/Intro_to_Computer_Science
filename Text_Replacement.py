###############################################
#       Exercise by Websten from forums       #
###############################################
# To minimize errors when writing long texts with
# complicated expressions you could replace 
# the tricky parts with a marker. 
# Write a program that takes a line of text and 
# finds the first occurrence of a certain marker 
# and replaces it with a replacement text. 
# The resulting line of text should be stored in a variable. 
# All input data will be given as variables.
#
# Replace the first occurrence of marker in the line below.
# There will be at least one occurrence of the marker in the
# line of text. Put the answer in the variable 'replaced'.
# You can find out the length of a string by command len(string)

# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

# Example 2 # uncomment this to test with different input
marker = "EY"
replacement = "Eyjafjallajokull"
line = "The eruption of the volcano EY in 2010 disrupted air travel in Europe for 6 days."

###

find_marker = line.find(marker)
before_marker = line[:find_marker]
after_marker = line[find_marker+len(marker):]
replaced = before_marker + replacement + after_marker

print(replaced)
# Example 1 output should be:
#>>> I will now go to sleep and be away from keyboard until lunch time tomorrow.
# Example 2 output should be:
#>>> The eruption of the volcano Eyjafjallajokull in 2010 disrupted air travel in Europe for 6 days.