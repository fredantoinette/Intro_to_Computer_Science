# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

def bigger(a,b):
    if a > b:
        return a
    return b
    
def smaller(a,b):
    if a < b:
        return a
    return b
    
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smallest(a,b,c):
    return smaller(a,smaller(b,c))

def set_range(x,y,z):
    return biggest(x,y,z) - smallest(x,y,z)
    


print(set_range(10, 4, 7))
#>>> 6  # since 10 - 4 = 6

print(set_range(1.1, 7.4, 18.7))
#>>> 17.6 # since 18.7 - 1.1 = 17.6