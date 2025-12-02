class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        val = len(nums) / 2
        for num in freq:
            if freq[num] > val:
                return num
        return -1