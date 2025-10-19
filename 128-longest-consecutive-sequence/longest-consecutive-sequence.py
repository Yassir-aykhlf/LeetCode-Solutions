class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0
        for num in seq:
            if num - 1 not in seq:
                count = 1
                while num + count in seq:
                    count += 1
                longest = max(longest, count)
        return longest