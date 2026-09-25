class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,cnt,ans=0,0,0
        n=len(s)
        vowel="aeiou"
        for i in range(k):
            if s[i] in vowel:
                cnt+=1
        ans=cnt
        for r in range(k,n):
            if s[r] in vowel:
                cnt+=1
            if r-l+1>k:
                if s[l] in vowel:
                    cnt-=1
                l+=1
            ans=max(ans,cnt)
        return ans