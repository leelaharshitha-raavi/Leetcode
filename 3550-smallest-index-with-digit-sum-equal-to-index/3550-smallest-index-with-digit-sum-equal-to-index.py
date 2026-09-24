class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            digsum=sum(int(c) for c in str(nums[i]))
            if digsum==i:
                ans=i
                break
        return ans