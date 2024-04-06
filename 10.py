def fibonacci(n, a=1, b=1, sequence=[]):
    if a > n:
        return sequence
    sequence.append(a)
    return fibonacci(n, b, a + b, sequence)

input_number = 5
output_sequence = fibonacci(input_number)
print(output_sequence)
