class Solution:
    def binSearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        for row in matrix:
            if self.binSearch(row, target):
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
sol = Solution()
print(sol.searchMatrix(matrix, 7))
