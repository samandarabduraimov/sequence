def count_integers(lst):
    count = 0
    for item in lst:
        if type(item) == int:
            count += 1
    return count

input_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
output = count_integers(input_list)
print(output)
