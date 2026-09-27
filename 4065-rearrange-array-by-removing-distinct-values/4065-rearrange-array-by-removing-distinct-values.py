class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        freq=Counter(nums)
        ans = []

        while freq:
            for num in sorted(freq):
                ans.append(num)
                freq[num] -= 1
                if freq[num]==0:
                    del freq[num]

        return ans