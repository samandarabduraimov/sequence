def find_max(lst):
    max_pair = max(lst[0])
    
    for pair in lst[1:]:
        max_pair = max(max_pair, max(pair))
    
    return max_pair

input_list = [[1, 5], [4, 8], [3, 6], [9, 2]]
output = find_max(input_list)
print(output)
