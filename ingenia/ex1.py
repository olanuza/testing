# Exercise 1

# Parse integer to digit list
def int2list(N):
    dlist = []
    for digit in str(N):
        dlist.append(int(digit))
    return dlist

print(int2list(12345))