# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            return binary_search(arr, target, start, middle_index-1)
        else:
            return binary_search(arr, target, middle_index+1, end)
    else:
        return -1
array = [2, 3, 4, 1, 8, 0, 9, 0, 7]
print(binary_search(array, 9, 0, 7))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
