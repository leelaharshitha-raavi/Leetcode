class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert(date):
            m,d=map(int,date.split("-"))
            tot=d
            for i in range(m-1):
                tot+=days[i]
            return tot
        a1=convert(arriveAlice)
        a2=convert(arriveBob)
        b1=convert(leaveAlice)
        b2=convert(leaveBob)
        start=max(a1,a2)
        end=min(b1,b2)
        if start>end:
            return 0
        return end-start+1