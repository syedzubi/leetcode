## The time complexity in the worst case is going to be O(n) 
## we dont use it much because it comes with constraints such as 1) there needs to be a finite value

def bucketSort(list1):
    count = [0,0,0]

    for n in range(len(list1)):
        count[list1[n]] += 1

    value = 0 
    for n in range(len(count)):
        for j in range(count[n]):
            list1[value] = n
            value += 1
    return list1

value = [2,1,2,0,0,2]
print(bucketSort(value))  