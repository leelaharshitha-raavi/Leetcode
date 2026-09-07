class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = {}
        for ch in s:
            new_dp = 2 * dp

            if ch in last:
                new_dp -= last[ch]

            last[ch] = dp

            dp = new_dp % MOD

        return (dp - 1) % MOD