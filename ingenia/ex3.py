# Exercise 3

# ex 1

def myLenghth(L):
    return len(L)

print(myLenghth([1,2,3,4,5]))

# ex 2

def myMaximum(L):
    return max(L)

print(myMaximum([1,2,3,4,5,4]))

# ex 3

def average(L):
    return sum(L)/len(L)    # could use myLength(L)

print(average([1,2,3,4,5,6,7,8,9]))

# ex 4

def buildPalindrome(L):
    pal = []
    for item in L:
        #pal = [item] + pal
        pal.insert(0,item)
    return pal

print(buildPalindrome([1,2,3,4,5]))

# ex 5

def remove (L1,L2):
    for item in L2:
        L1.remove(item)
    return L1

print(remove([1,2,3,4,5],[2,4]))

# ex 6

def flatten(L):
    return recursive_flat(L, [])

def recursive_flat(L, flat_list):
    for item in L:
        if isinstance(item, list):
            recursive_flat(item, flat_list)
        else:
            flat_list.append(item)
    return flat_list

print (flatten([1,[2,[3,4]]]))

# ex 7

def oddsNevens(L):
    odds = []
    evens = []
    for item in L:
        if item%2==0:
            odds.append(item)
        else:
            evens.append(item)
    return odds, evens

print(oddsNevens([1,2,3,4,5]))

# ex 8

def isPrime(n):
    return 2 in [n,2**n%n]

def primeDivisors(n):
    if n>0:
        prime_div = []
        div = n
        while (div>0):
            if (n%div==0 and isPrime(div)):
                prime_div.append(div)
            div-=1
        prime_div.append(1)    
        return prime_div
    else:
        return ('Error: insert non-zero positive integer.')

print(primeDivisors(45678))

# ex 9

def is_increasing(L):
    return 0