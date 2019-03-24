# Exercise 1


# Minimal version of valencia function. As we compare absolute number, sum order is not important
def valencia_min(N):
    odd = 0
    even = 0
    for position, digit in enumerate(str(N)):
        if ((position%2)==0):
            even += int(digit)
        else:
            odd += int(digit)
    return((odd-even)==0)

print("TRUE", valencia_min(111111))
print("FALSE", valencia_min(1111111))