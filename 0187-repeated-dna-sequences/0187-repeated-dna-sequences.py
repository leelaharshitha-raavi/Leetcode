class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        freq={}
        ans=[]
        for i in range(len(s)-9):
            sub=s[i:i+10]
            freq[sub]=freq.get(sub,0)+1
            if freq[sub]==2:
                ans.append(sub)
        return ans