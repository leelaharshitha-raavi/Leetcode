class Solution:
    def func(self,i,j,s,t,dp):
        if j<0:return 1
        if i<0:
            return 0
#the order of j and i  must be followewd here otherwise no execution happend 
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            dp[i][j]=self.func(i-1,j-1,s,t,dp)+self.func(i-1,j,s,t,dp)
        else:
            dp[i][j]=self.func(i-1,j,s,t,dp)
        return dp[i][j]
        
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        return self.func(n-1,m-1,s,t,dp)