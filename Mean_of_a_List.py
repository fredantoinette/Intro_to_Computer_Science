# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

def list_mean(a):
    if a != []:
        n = len(a)
        sum = 0.0
        for i in range(n):
            sum = sum + a[i]
        return sum/n
    else:
        return "???"

print(list_mean([1,2,3,4]))
#>>> 2.5
print(list_mean([1,3,4,5,2]))
#>>> 3.0
print(list_mean([]))
#>>> ???
print(list_mean([2]))
#>>> 2.0