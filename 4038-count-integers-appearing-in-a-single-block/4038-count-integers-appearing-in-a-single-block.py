class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen=set()
        bad=set()
        for i in range(len(nums)):
            if i>0 and nums[i]!=nums[i-1]:
                if nums[i] in seen:
                    bad.add(nums[i])
                else:
                    seen.add(nums[i])
            if i==0:
                seen.add(nums[i])
        return len(seen)-len(bad)