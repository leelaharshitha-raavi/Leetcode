class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a,b,c=0,1,1
        for i in range(n):
            if a+b+c==n:
                return True
            if b+c>n:
                return False
            a=b
            b=c
            c=a+b
        return False
