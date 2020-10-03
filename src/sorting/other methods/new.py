# ----- Not Efficient ----
# maximum recursion depth exceeded while calling a Python object
def merge(L, R):
    arr = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j])
            j += 1
    return arr + L[i:] + R[j:]

array1 = [2, 4]
array2 = [1, 3]
print(merge(array1, array2))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]
        return merge(merge_sort(L), merge_sort(R))

myarr= [2,4,6,1,9,5,3]
print(merge_sort(myarr))
  