class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def backtrack(cur,opencnt,closecnt):
            if len(cur)==2*n:
                ans.append(cur)
                return ans
            if opencnt<n:
                backtrack(cur+"(",opencnt+1,closecnt)
            if closecnt<opencnt:
                backtrack(cur+")",opencnt,closecnt+1)
        backtrack("",0,0)
        return ans