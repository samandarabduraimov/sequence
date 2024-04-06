def find_largest_sum_list(lst):
    max_sum = sum(lst[0])
    max_list = lst[0]

    for sub_list in lst[1:]:
        current_sum = sum(sub_list)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = sub_list

    return max_list

list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
result = find_largest_sum_list(list)
print(result)
