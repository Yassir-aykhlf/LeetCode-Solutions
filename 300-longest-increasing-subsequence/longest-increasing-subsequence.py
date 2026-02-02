class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for n in nums:
            idx = bisect.bisect_left(LIS, n)
            if idx == len(LIS):
                LIS.append(n)
            else:
                LIS[idx] = n
        return len(LIS)