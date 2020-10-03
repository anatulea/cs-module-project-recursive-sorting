def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = arrA + arrB

    # Your code here
    some_num1 = some_num2 = some_num3 = 0

    while some_num1 < len(arrA) and some_num2 < len(arrB):
        if arrA[some_num1] <= arrB[some_num2]:
            merged_arr[some_num3] = arrA[some_num1]
            some_num1 += 1
        else:
            merged_arr[some_num3] = arrB[some_num2]
            some_num2 += 1
        some_num3 += 1

    while some_num1 < len(arrA):
        merged_arr[some_num3] = arrA[some_num1]
        some_num1 += 1
        some_num3 += 1

    while some_num2 < len(arrB):
        merged_arr[some_num3] = arrB[some_num2]
        some_num2 += 1
        some_num3 += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        if len(left) > 1:
            left = merge_sort(left)
        if len(right) > 1:
            right = merge_sort(right)

        arr = merge(left, right)

    return arr