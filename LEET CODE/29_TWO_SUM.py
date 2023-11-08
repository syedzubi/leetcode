class Solution:
    def twoSum(self, nums, target):
        prevDict = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in prevDict:
                return [prevDict[diff], i]
            prevDict[n] = i
        return False
