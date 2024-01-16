# # /* 
#   Given an array of strings
#   return the number of times each string occurs (a frequency / hash table)
# */

arr1 = ["a", "a", "a"]


arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"]

arr3 = []
expected3 = {}


def makeFrequencyTable(arr):
    empty = {}
    for i in arr:
        # print(empty[i])
        if empty.get(i) is None:
            empty[i] = 1






    # i=0
    # while i < arr:
    #     print(arr[i])
    #     i+=1


makeFrequencyTable(arr1)
makeFrequencyTable(arr2)
makeFrequencyTable(arr3)


