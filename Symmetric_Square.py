# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
    
def symmetric(a):
    n = len(a)
    for i in range(n):
        same = 0
        for j in range(n):
            if a[i][j] == a[j][i]:
                same = same + 1
        if same != n:
            return False
        if len(a[0]) != n:
            return False
    return True
    
print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
#>>> True


print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False

print(symmetric([[1, 2],
                [2, 1]]))
#>>> True

print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
#>>> False

print(symmetric([[1,2,3],
                 [2,3,1]]))
#>>> False

# additional test
print(symmetric([]))
#>>> True