class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for index, char in enumerate(s, start=1):
            reverse_rank = 26 - (ord(char) - ord('a'))
            total_degree += reverse_rank * index
        return total_degree