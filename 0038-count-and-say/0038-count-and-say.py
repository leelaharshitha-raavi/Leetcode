class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        if n==1:
            return s
        for _ in range(n-1):
            res=""
            cnt=1
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    cnt+=1
                else:
                    res+=str(cnt)+s[i-1]
                    cnt=1
            res+=str(cnt)+s[-1]
            s=res
        return s

