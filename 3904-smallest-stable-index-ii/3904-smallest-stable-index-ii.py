class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if n==1:
            return 0
        pre,suf=[0]*n,[0]*n
        pre[0]=nums[0]
        suf[n-1]=nums[n-1]
        mini=-1
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suf[i]=min(suf[i+1],nums[i])
        for i in range(n):
            s=pre[i]-suf[i]
            if s==0:
                return i
            if s<=k:
                mini=i
                break
        return mini