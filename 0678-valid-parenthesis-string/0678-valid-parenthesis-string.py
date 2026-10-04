'''class Solution:
    def isValid(self,s,index,cnt):
        if cnt<0:
            return False
        if index==len(s):
            return cnt==0
        c=s[index]
        if c=='(':
            return self.isValid(s,index+1,cnt+1)
        elif c==')':
            return self.isValid(s,index+1,cnt-1)
        else:
            return self.isValid(s,index+1,cnt) or self.isValid(s,index+1,cnt+1) or self.isValid(s,index+1,cnt-1)
    def checkValidString(self, s: str) -> bool:
        return self.isValid(s,0,0)---------time limit exceeded'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0#return true only if no paranthesis left


        