# Problem Link: https://www.hackerrank.com/challenges/countingsort2/problem


def countingSort(arr):
    indexCount = [0]*(max(arr) + 1)
    for i in arr:
        indexCount[i] += 1
    sortedArr = []
    for i in range(len(indexCount)):
        sortedArr += [i]*indexCount[i]
    return sortedArr


arr1 = [1, 1, 3, 2, 1]
arr2 = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32]
print(countingSort(arr2))
