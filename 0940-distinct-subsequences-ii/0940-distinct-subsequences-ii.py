class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=1
        last={}
        MOD=int(10e9)
        for ch in s:
            new_dp=dp*2
            if ch in last:
                new_dp-=last[ch]
            last[ch]=dp
            dp=new_dp%MOD
        return (dp-1)%MOD