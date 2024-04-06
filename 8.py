def add_x_to_list(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(lst2[i] + ' ' + str(lst1[i]))
    return result

list1 = [1, 4, 3, 9]
list2 = ['chelsea', 'real', 'barca', 'MU']
output = add_x_to_list(list1, list2)
print(output)
