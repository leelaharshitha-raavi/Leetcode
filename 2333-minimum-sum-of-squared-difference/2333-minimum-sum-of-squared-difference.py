class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            need = sum(max(0, d - mid) for d in diff)

            if need <= k:
                right = mid
            else:
                left = mid + 1

        limit = left

        remaining = k
        for i in range(len(diff)):
            reduction = max(0, diff[i] - limit)
            diff[i] -= reduction
            remaining -= reduction
        diff.sort(reverse=True)

        for i in range(len(diff)):
            if remaining == 0:
                break
            if diff[i] > 0:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)