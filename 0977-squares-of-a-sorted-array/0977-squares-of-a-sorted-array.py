class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr=[x**2 for x in nums]
        arr.sort()
        return arr