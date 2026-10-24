class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        sr=source[0]
        sc=source[1]
        tr=target[0]
        tc=target[1]
        if sr==tr and sc==tc:
            return 0
        if (sr==tr or sc==tc or abs(tr-sr)==abs(tc-sc)):
            return 1
        return 2