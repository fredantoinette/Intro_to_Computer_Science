# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(total_seconds):
    hour = int(total_seconds / 3600)
    if hour != 1:
        h = "hours"
    else:
        h = "hour"    
    minute = int(total_seconds % 3600 / 60)
    if minute != 1:
        m = "minutes"
    else:
        m = "minute"
    second = round(total_seconds - minute * 60 - hour * 3600, 1)
    if second - int(second) == 0:
        second = int(second)
    if second != 1:
        s = "seconds"
    else:
        s = "second"
    return str(hour) + " " + h + ", " + str(minute) + " " + m + ", " + str(second) + " " + s
    
print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds


