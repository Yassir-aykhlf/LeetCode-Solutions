class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for n in nums:
            if freq[n] == len(nums) // 2:
                return n