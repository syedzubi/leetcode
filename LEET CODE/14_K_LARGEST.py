class Solution:
    # def findKthLargest(self, nums, k) -> int:
    #     nums.sort()
    #     return nums[len(nums)-k]
    def findKthLargest(self, nums, k) -> int:
        k = len(nums) - k

        def quickSelect(l,r):
            pivot,p = nums[r],l

            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i],nums[p] = nums[p], nums[i]
                    p += 1
            nums[p],nums[r] = nums[r], nums[p]

            if k > p:
                return quickSelect(p + 1, r)
            elif k < p:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
             
        return quickSelect(0, len(nums) - 1)
    
sol = Solution()
print(sol.findKthLargest([9,7,2,5,1,2],1))