class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, t: int) -> int:
        cnt=0
        tot=0
        n=len(arr)
        for i in range(k):
            tot+=arr[i]
        avg=tot//k
        if avg>=t:
            cnt=1
        for r in range(k,n):
            tot+=arr[r]-arr[r-k]
            avg=tot//k
            if avg>=t:
                cnt+=1
        return cnt