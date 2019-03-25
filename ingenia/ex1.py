# Exercise 1


# Minimal version of valencia function. As we compare absolute number, sum order is not important
def valencia(N):
    odd = 0
    even = 0
    for position, digit in enumerate(str(N)):
        if ((position%2)==0):
            even += int(digit)
        else:
            odd += int(digit)
    return(abs(odd-even))

# Check valencia's value of sequence of numbers
def check_valencia(L):
    max_val = 0    # store valencia
    for number in L:
        x = valencia(number)
        if x==0:
            return number
        else:   # if higher val, store valencia
            if x>max_val:
                max_val = x
    return max_val

seq1 = [15742, 15743, 1111, 15744, 2222, 15745]
seq2 = [15742, 15743, 15744, 15745]

print(check_valencia(seq1))
print(check_valencia(seq2))