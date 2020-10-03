# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(a, l, m, r):
    # Your code here\
    n1 = m - l + 1
    n2 = r - m  
    L = [0] * n1  
    R = [0] * n2  
    for i in range(0, n1):  
        L[i] = a[l + i]  
    for i in range(0, n2):  
        R[i] = a[m + i + 1]  
  
    i, j, k = 0, 0, l  
    while i < n1 and j < n2:  
        if L[i] > R[j]:  
            a[k] = R[j]  
            j += 1
        else:  
            a[k] = L[i]  
            i += 1
        k += 1
  
    while i < n1:  
        a[k] = L[i]  
        i += 1
        k += 1
  
    while j < n2:  
        a[k] = R[j]  
        j += 1
        k += 1


def merge_sort_in_place(a):
    # Your code here
    current_size = 1
      
    # Outer loop for traversing Each  
    # sub array of current_size  
    while current_size < (len(a) - 1):  
          
        left = 0
        # Inner loop for merge call  
        # in a sub array  
        # Each complete Iteration sorts  
        # the iterating sub array  
        while left < len(a)-1:  
              
            # mid index = left index of  
            # sub array + current sub  
            # array size - 1  
            mid = min((left + current_size - 1),(len(a)-1)) 
              
            # (False result,True result)  
            # [Condition] Can use current_size  
            # if 2 * current_size < len(a)-1  
            # else len(a)-1  
            right = ((2 * current_size + left - 1,  
                    len(a) - 1)[2 * current_size  
                        + left - 1 > len(a)-1])  
                              
            # Merge call for each sub array  
            merge_in_place(a, left, mid, right)  
            left = left + current_size*2
              
        # Increasing sub array size by  
        # multiple of 2  
        current_size = 2 * current_size  


# Driver code  
a = [12, 11, 13, 5, 6, 7] 
print("Given array is ")  
print(a)  
  
merge_sort_in_place(a)  
  
print("Sorted array is ")  
print(a) 