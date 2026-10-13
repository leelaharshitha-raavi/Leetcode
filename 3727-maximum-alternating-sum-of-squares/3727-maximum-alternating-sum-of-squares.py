
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        tot = 0
        n = len(nums)
        for i in range(n // 2):
            tot += nums[n - 1 - i] ** 2
            tot -= nums[i] ** 2
        if n % 2 == 1:
            tot += nums[n // 2] ** 2
        return tot

