# Remove duplicates from a sorted array
# you cannot allocate a new array , need to modify the existing one

myArray = [10, 20, 20, 30, 30, 50, 60, 70, 70, 70]

left = 1

for right in range(1, len(myArray)):
    if myArray[right] != myArray[right-1]:
        myArray[left] = myArray[right]
        left += 1

print(left,myArray)
