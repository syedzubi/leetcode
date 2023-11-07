# 1) READING FROM AN ARRAY

myArray = [10, 20, 30]
# print(myArray[1])

# 2) TRAVERSING THROUGH AN ARRAY

# for elem in range(len(myArray)):
#     print(myArray[elem])

# i = 0
# while i < len(myArray):
#     print(myArray[i])
#     i += 1

# 3) DELETING FROM THE END OF THE ARRAY
# you can a delete a value  by setting the value to 0/ null or -1 THIS DOES THE JOB


def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0

 # 4) DELETING AT THE iTH INDEX


def removeMiddle(arr, length, i):
    # Shift the rest of the values to the left after deleting is completed
    # Shift starting from i + 1 to end.
    for index in range(i+1, length):
        arr[index-1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted

# 5) INSERTING AT THE END
# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).


def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

# 6) INSERTING AT THE ith INDEX


def insertMiddle(arr, n, length, i):
    # move all the elements to the right
    for index in range(length-1, i-1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n
    return arr

# print(insertMiddle([10,20,30,40,0,0], 80, 4, 0, 6))
