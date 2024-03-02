class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)

        for x in range(n):
            ans[x] = nums[x]
            ans[x + n] = nums[x]

        return ans
