def arifmetik(list1, list2):
    total = sum(list1)
    count = len(list1)
    for num in list2:
        if num not in list1:
            total += num
            count += 1
    return total / count

# Test
list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
print(arifmetik(list1, list2))
