class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left=0
        right=n-1
        index=n-1
        arr=[0]*n
        while left<=right:
            if nums[left]**2>nums[right]**2:
                arr[index]=nums[left]**2
                index-=1
                left+=1
            else:
                arr[index]=nums[right]**2
                index-=1
                right-=1
        return arr

        
