# By Dimitris_GR from forums
# Return True if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.
    
def antisymmetric(A):
    n = len(A)
    for i in range(n):
        anti = 0
        for j in range(n):
            if A[i][j] == -A[j][i]:
                anti = anti + 1
        if anti != n:
            return False
        if len(A[0]) != n:
            return False
    return True


# Test Cases:

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]]))   
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False


