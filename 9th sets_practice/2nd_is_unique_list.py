def is_unique_list(lst):
    return lst == list(set(lst))

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False