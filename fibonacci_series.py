# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a,b = 0,1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

def fibonacci_series(nterm):
    a, b = 0, 1
    count = 0
    if nterm < 0:
        pass
    elif nterm == 0:
        print(0, end=" ")
    elif nterm == 1:
        print(1, end=" ")
    else:
        while count < nterm:
            print(a, end=" ")
            c = a + b
            a = b
            b = c
            count += 1
# Driver Program
# print(fibonacci(9))
print(fibonacci_series(10))