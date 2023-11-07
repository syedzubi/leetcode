# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1
#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp


# RIAZ METHOD
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * (n+1)
#         if n <= 1:
#             return 1
#         elif n == 2:
#             return 2
#         dp[0], dp[1], dp[2] = 0, 1, 2

#         for i in range(3, n):
#             dp[i] = dp[i-1] + dp[i-2]

#         return dp[n]
    
class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
