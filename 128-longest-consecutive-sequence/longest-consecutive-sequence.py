class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        max_len = 0
        for num in nums_s:
            if num - 1 not in nums_s:
                cur_len = 1
                while num + cur_len in nums_s:
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len