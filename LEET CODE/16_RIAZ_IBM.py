### 

list1 = [1,2,3,4,5,6,7,8,9]

list2 = [[1,2], [3,4], [1,6]]

for list_ in list2:
    for value in range(list_[0] -1, list_[1]):
        list1[value] = list1[value] * -1

print(list1)