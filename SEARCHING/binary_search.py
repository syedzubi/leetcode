def binarySearch(arr, target):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        middle_value = arr[mid]
        if target == middle_value:
            return True
        elif target > middle_value:
            low = mid + 1
        elif target < middle_value:
            high = mid - 1
    return False

values = [10,20,30,40,50,60,70,80,90,100]

print(binarySearch(values, 101))
