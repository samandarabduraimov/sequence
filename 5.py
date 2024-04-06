def most_element(lst):
    max_count = 0
    most_common = None

    for num in lst:
        current_count = lst.count(num)
        if current_count > max_count:
            max_count = current_count
            most_common = num

    return most_common, max_count

input_list = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
frequency = most_element(input_list)
print( frequency)
