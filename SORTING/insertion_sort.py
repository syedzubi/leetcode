def insertionsort(list1):
    for i in range(1, len(list1)):
        j = i - 1
        while j >=0 and list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
            j -= 1
    return list1

print(insertionsort([2,3,4,1,6,0,4,7,8,9,1,1,1,2,3,4,-9,-8,-3])) 