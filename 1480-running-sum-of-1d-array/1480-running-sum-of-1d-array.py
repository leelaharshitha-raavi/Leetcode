class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        tot=0
        n=len(nums)
        arr=[0]*n
        for i in range(n):
            tot+=nums[i]
            arr[i]=tot
        return arr
            