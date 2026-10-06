class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bracket=0
        ans=0
        for char in s:
            if char=="(":
                bracket+=1
            else:
                if bracket>0:
                    bracket-=1
                else:
                    ans+=1
        return bracket+ans