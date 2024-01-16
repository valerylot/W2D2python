# # /* 
#   Given an array of strings
#   return the number of times each string occurs (a frequency / hash table)
# */

arr1 = ["a", "a", "a"]


arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"]

arr3 = []
expected3 = {}


def make_frequency_table(arr):
    frequency_table = {}

    for val in arr:
        if val not in frequency_table:
            frequency_table[val] = 1
        else:
            frequency_table[val] += 1

    return frequency_table


arr1 = ["a", "a", "a"]
expected1 = {"a": 3}

arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"]
expected2 = {"a": 2, "b": 1, "c": 3, "B": 1, "d": 1}

arr3 = []
expected3 = {}

print(make_frequency_table(arr1))
print(make_frequency_table(arr2))
print(make_frequency_table(arr3))

