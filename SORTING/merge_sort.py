def merge(l1, l2):
    i = j = 0
    merged_list = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
    while i < len(l1):
        merged_list.append(l1[i])
        i += 1
    while j < len(l2):
        merged_list.append(l2[j])
        j += 1
    return merged_list-------------

def mergeSort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    return merge(mergeSort(unsorted_list[:middle]), mergeSort(unsorted_list[middle:]))