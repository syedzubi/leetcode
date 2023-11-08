class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()
        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False
        hashset = {}
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset[num] = 1
        return False
