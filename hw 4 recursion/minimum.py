def minRec(arr, n):
    # base case: if array has only one element, return it
    if n == 1:
        return arr[0]
    # recursive case: find minimum of the rest of the array and compare with the first element
    return min(arr[0], minRec(arr[1:], n-1))
arr = [3, 5, 3, 7, 2]
n = len(arr)
min_element = minRec(arr, n)
print(min_element)
