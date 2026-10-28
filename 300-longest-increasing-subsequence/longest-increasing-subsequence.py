class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = []
        for n in nums:
            idx = bisect.bisect_left(lis, n)
            if idx == len(lis):
                lis.append(n)
            else:
                lis[idx] = n
        return len(lis)