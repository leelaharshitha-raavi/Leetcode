class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        left=0
        cur_Sum=0
        maxi=-1
        for right in range(len(nums)):
            cur_Sum+=nums[right]
            while cur_Sum>target:
                cur_Sum-=nums[left]
                left+=1
            if cur_Sum==target:
                maxi=max(maxi,right-left+1)
        if maxi==-1:
            return -1
        return len(nums)-maxi