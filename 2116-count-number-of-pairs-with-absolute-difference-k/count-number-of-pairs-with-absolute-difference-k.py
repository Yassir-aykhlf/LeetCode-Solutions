class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = collections.Counter(nums)
        count = 0
        for num in freq:
            if num + k in freq:
                count += freq[num + k] * freq[num]
        return count