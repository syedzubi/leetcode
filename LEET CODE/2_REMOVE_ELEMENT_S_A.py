
myArray = [0,1,2,2,3,0,4,2]
val = 2

left = 0

for right in range(len(myArray)):
    if myArray[right] != val:
        myArray[left] = myArray[right]
        left += 1
print(myArray)