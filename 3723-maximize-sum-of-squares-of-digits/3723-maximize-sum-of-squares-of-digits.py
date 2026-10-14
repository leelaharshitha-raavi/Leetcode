class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum==0 or sum>9*num:
            return ""
        ans=""
        for i in range(num):
            digit=min(9,sum)
            ans+=str(digit)
            sum-=digit
        return ans