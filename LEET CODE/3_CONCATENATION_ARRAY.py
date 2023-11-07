def getConcatenation(nums,x):
    ans = []
    for i in range(x):
        for num in nums:
            ans.append(num)
    return ans

print(getConcatenation([1,2,3,4], 4))