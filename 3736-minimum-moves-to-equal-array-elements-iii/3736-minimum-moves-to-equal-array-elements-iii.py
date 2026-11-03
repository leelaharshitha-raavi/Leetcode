class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves=0
        maxi=max(nums)
        for num in nums:
            moves+=abs(num-maxi)
        return moves