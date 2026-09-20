class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        n = len(intervals)
        for i in range(n):
            for j in range(i + 1, n):
                if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                    count += 1
        return count