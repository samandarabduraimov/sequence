def add(lst, prefix):
    result = [prefix + str(item) for item in lst]
    return result

list = [1, 4, 3, 9]
string = "RM"
output = add(list, string)
print(output)
