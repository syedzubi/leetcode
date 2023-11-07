# def partition(array, low , high):

#     pivot = array[high]
#     i = low
#     for j in range(low, high):
#         if array[j] <= pivot:
#             array[i], array[j] = array[j], array[i]
#             i = i + 1
#     array[i], array[high] = array[high], array[i]
#     return i

# def quicksort(array , low, high):
#     if low < high:
#         pi_index = partition(array, low , high)
#         quicksort(array, low, pi_index - 1)
#         quicksort(array, pi_index + 1, high)
#     return array

class Solution:
    def swap(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        
    def partition(self, array, low, high):
        i = low
        pivot = array[high]
        for j in range(low, high):
            if array[j] <= pivot:
                self.swap(array, i, j)
                i += 1
        
        self.swap(array, i, high)

        return i
    
    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low , pi -1)
            self.quickSort(array, pi + 1, high)
        return array

    def sortArray(self, nums):
        return self.quickSort(nums, 0, len(nums)-1)

s_obj = Solution()
print(s_obj.sortArray([7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,
                       4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,
                       5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,
                       5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,
                       7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,
                       4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,
                       5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,
                       5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,
                       7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,
                       4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,
                       5,9,7,6,5,2,3,5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,
                       5,6,7,8,9,0,1,7,2,1,4,7,6,5,4,9,8,7,1,2,3,5,9,7,6,5,2,3,5,6,7,8,9,0,1]))
