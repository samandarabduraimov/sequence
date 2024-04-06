def inumber(lst):
    n = len(lst)
    number = 0
    for i in range(n):
        number += lst[i] * 10 ** (n - i - 1)
    number += 1
    result = []
    while number > 0:
        result.insert(0, number % 10)
        number //= 10
    if result[0] == 0:
        result.insert(0, 1)
    return result

inputs = [
    [1,2,3],
    [9],
    [9,9,9,9]
]

for input_list in inputs:
    print(f"Input: {input_list}")
    output_list = inumber(input_list)
    print(f"Output: {output_list}")
