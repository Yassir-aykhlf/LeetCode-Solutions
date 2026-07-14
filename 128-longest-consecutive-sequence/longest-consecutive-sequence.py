class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = set(nums)
        res = 0
        for n in nums_:
            if n - 1 not in nums_:
                count = 1
                while n + count in nums_:
                    count += 1
                res = max(res, count)
        return res