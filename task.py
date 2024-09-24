as_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

as_list_second = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

for el in as_list:
    if el < 5:
        print(el)

print(list(set(as_list_second) & set(ba)))
unique_values = list(set(arr) ^ set(bar))
print(unique_values)
