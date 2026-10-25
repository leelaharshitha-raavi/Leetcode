class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def findset(num):
            cnt=0
            while num>0:
                if num%2==1:
                    cnt+=1
                num//=2
            return cnt
        s1=findset(a)
        s2=findset(b)
        if s1>=s2:
            return s1*s2
        return s2//s1