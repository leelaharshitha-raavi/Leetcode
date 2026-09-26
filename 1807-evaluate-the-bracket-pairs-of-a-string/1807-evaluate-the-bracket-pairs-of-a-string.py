class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans=""
        i=0
        n=len(s)
        mp=dict(knowledge)
        while i<n:
            if s[i]!="(":
                ans+=s[i]
                i+=1
            else:
                new=""
                i+=1
                while s[i]!=")":
                    new+=s[i]
                    i+=1
                ans+=mp.get(new,"?")
                i+=1
        return ans