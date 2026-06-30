# exe3: print first 10 Fibonacci numbers within the range of 10

limit = 10
fibonacci = [0, 1]

while len(fibonacci) < 10:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)
