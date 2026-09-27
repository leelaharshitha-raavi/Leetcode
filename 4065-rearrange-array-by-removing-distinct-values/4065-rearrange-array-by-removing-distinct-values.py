class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        ans = []

        while freq:
            for num in sorted(freq):
                ans.append(num)
                freq[num] -= 1

            # Remove numbers whose frequency became 0
            freq = {num: cnt for num, cnt in freq.items() if cnt > 0}

        return ans