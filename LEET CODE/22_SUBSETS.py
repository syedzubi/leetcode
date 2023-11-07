"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            ##left side of the tree || decision to include the value in nums[i]
            subset.append(nums[i]) 
            dfs(i+1)

            ##right side of the tree || decision to NOT include the value in nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res