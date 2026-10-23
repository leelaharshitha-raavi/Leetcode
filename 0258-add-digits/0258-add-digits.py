class Solution:
    def addDigits(self, num: int) -> int:
        val=0
        while len(str(num))!=1:
            val=sum(int(ch) for ch in str(num))
            num=val
        return num