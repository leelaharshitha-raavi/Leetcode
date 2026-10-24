class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        cnt=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                cnt+=1
                continue
        return cnt