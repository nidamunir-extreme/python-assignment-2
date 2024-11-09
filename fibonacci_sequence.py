def fibonacci_sequence(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]


print(fibonacci_sequence(8))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
