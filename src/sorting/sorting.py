# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = arrA + arrB
    # Your code here
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here\
    # start of second array
    start2 = mid+1
    # If the direct merge is already sorted
    if arr[mid]<= arr[start2]:
        return 
    # Two pointers to maintain start 
    # of both arrays to merge
    while start <= mid and start2 <= end:
        if arr[start]<= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index= start2

            while index != start:
                arr[index] =arr[index -1]
                index -= 1
            arr[start] = value
            start +=1
            mid += 1
            start2 += 1

    
def merge_sort_in_place(arr, l, r):
    # Your code here
    if l<r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        
        merge_in_place(arr, l, m,r)
